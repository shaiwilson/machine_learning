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

@app.route('/welcome')
def train():
    """Train image data."""


    gl.canvas.set_target('browser')
    image_train = graph_lab.my_batch_job('seed_data/image_train_data/')

    # test a generic model for cats
    knn_model = graph_lab.knn_model_generic(image_train)
    cat = image_train[18:19]
    img_neighbors = graph_lab.get_images_from_ids(image_train, knn_model.query(cat))
  
    images = [[] for i in range(len(img_neighbors))]
    np_image_array = img_neighbors['image_array'].to_numpy()
    print type(np_image_array)
    print np_image_array.shape
    

   
    # for i, v in enumerate(np_image_array):
    #     # print "i is: " , i
    #     # print "v is: " , v
    #     print v 
    #     img_reshaped = np.reshape(v, (32,32,3))


    #     img = Image.fromarray(img_reshaped, 'RGB')
    #     img_index = str(i)
    #     img_name = "img_" + img_index 
    #     img.save('static/imgs/' + img_name + ".PNG")
    #     image_path = 'static/imgs/' + img_name + ".PNG" 
    #     images[i] = image_path
  

    return render_template("welcome.html")

# button on the welcome page that redirects to the show page
@app.route('/show')
def get_images(img_neighbors):
    """ Call show image function """

    images = show_list(img_neighbors)
    
    return render_template("imagelist.html", images=images)

def show_list(img_neighbors):
    """Show grid images."""

    # img_neighbors is a numpy array of images
    # images is an empty list of dictionary images
    images = [[] for i in range(len(img_neighbors))]
    np_image_array = img_neighbors['image_array'].to_numpy()
    print img_neighbors['image_array']

    format = 'PNG'
    for i, v in enumerate(np_image_array):
        # print "i is: " , i
        # print "v is: " , v
        print v 
        img_reshaped = np.reshape(v, (32,32,3))


        img = Image.fromarray(img_reshaped, 'RGB')
        img_index = str(i)
        img_name = "img_" + img_index 
        img.save('static/imgs/' + img_name + ".PNG")
        image_path = 'static/imgs/' + img_name + ".PNG" 
        images[i] = image_path
  
    return images 

@app.route('/cats')
def show_cats(image_train):
    """Show cat images."""

    cat = image_train[18:19]
    knn_model = graph_lab.knn_model_generic(image_train)
    cat_neighbors = graph_lab.get_images_from_ids(image_train, knn_model.query(cat))
    print cat_neighbors


@app.route('/show')
def view_method():
    response = send_file(tempFileObj, as_attachment=True, attachment_filename='myfile.jpg')
    return response

@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

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

    # # get form variables
    # new_tag = request.form["tag"]
    # image_id = request.form["image_id"]
    # if not tag:
    #     raise Exception("No tag given")


# SHOW ALL ROUTES

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