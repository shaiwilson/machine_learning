""" Product Recommender """

# Author: Shai Wilson

from jinja2 import StrictUndefined

# from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import connect_to_db, db, Image, Tag, Image_Tags
from array import array
from PIL import Image
import numpy as np
import graphlab as gl
import graph_lab

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_welcome():
    """ Show the homepage """

    return render_template("welcome.html")

def train():
    """Train image data."""

    image_train = graph_lab.my_batch_job('seed_data/image_train_data/')

    # test a generic model 
    knn_model = graph_lab.knn_model_generic(image_train)


    # this needs to change with the images
    cat = image_train[18:19]

    # get nearest neighbors
    img_neighbors = graph_lab.get_images_from_ids(image_train, knn_model.query(cat))
  
    return img_neighbors

@app.route('/show')
def get_images():
    """ Collect images to be shown. """

    img_neighbors = train()

    images = []
    
    for i, v in enumerate(img_neighbors['image_array']):
        np_image_array = img_neighbors['image_array'][i]
        images.append(np_image_array)

    images = show_list(img_neighbors)
    
    return render_template("imagelist.html", images=images)

def show_list(img_neighbors):
    """Convert pixel data to img format."""

    # img_neighbors is a list of dictionaries
    # imgages will hold the image_array for each image
    images = [[] for i in range(len(img_neighbors))]

    # basewidth = 300
    # maxsize = (1028, 1028)
    # image.thumbnail(maxsize, Image.ANTIALIAS)

    for i, v in enumerate(img_neighbors):
        pixel_array = v.get('image_array')
        new_np_array = np.array(pixel_array)
        img_reshaped = np.reshape(pixel_array, (32, 32, 3))
        width, height, numChan = img_reshaped.shape
        img = Image.fromarray(np.uint8(img_reshaped))
        # img.show()
        img_index = str(i)
        img_name = "img_" + img_index

        # img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save('static/imgs/' + img_name + ".PNG")
        image_path = img_name + ".PNG" 
        images[i] = image_path
  
    return images 

@app.route('/cats')
def show_cats(image_train):
    """Show cat images."""

    cat = image_train[18:19]
    knn_model = graph_lab.knn_model_generic(image_train)
    cat_neighbors = graph_lab.get_images_from_ids(image_train, knn_model.query(cat))
    print cat_neighbors


@app.route('/search')
def show_search_form():
    """Search page."""



    return render_template("search.html")


@app.route('/search_tags', methods=["POST"])
def search_db():
    """Search page."""

    text_query = request.form["query"]
    print text_query
    return render_template("search.html")

    # image_ids = Image.query.filter_by(image_label=text_query).all()


    # return render_template("results.html")


# ADD UPDATE DB
@app.route("/images/<int:image_id>", methods=['POST'])
def add_tag():
    """Add/edit a tag"""

    # Get form variables
    tag_label = request.form["query"]
    image_id = request.form["image_id"]

    if not image_id:
        raise Exception("No image to tag")

    all_tags = Image_Tags.query.filter_by(image_id=image_id).all()

    if all_tags:
        # add new tag to list of tags stored in db
        flash("Tag added.")

    else:
        # add new tag list to database
        tag_label = Tag(tag_label=tag_label)
        flash("Rating added.")
        db.session.add(all_tags)

    db.session.commit()

    return redirect("/images/%s" % image_id)


@app.route("/tags")
def tag_list():
    """Show list of tags."""

    tags = Tag.query.all()
    return render_template("tags_list.html", tags=tags)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
    connect_to_db(app)
    gl.canvas.set_target('browser')

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()