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
    cat_neighbors = graph_lab.get_images_from_ids(image_train, knn_model.query(cat))

    # graph_lab.show_images(cat_neighbors, 'image') 
    # cat_neighbors['image'].show()

    # first version
    print cat_neighbors['image_array']
    print "***********************"

    cat_neighbors["image_show"] = cat_neighbors['image_array'].pixel_array_to_image(32, 32, 3, allow_rounding = True)
    print cat_neighbors
    # print images
    image_array = np.array(cat_neighbors['image_array'])
    result = array2PIL(image_array, len(cat_neighbors['image_array']))


    return render_template("welcome.html")

def array2PIL(arr, size):
        mode = 'RGBA'
        arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
        if len(arr[0]) == 3:
            arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
        return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)



# what do u do when the dictionary key is a tuple, first item 
# is a string and the second item is a list of ints

@app.route("/images")
def image_list(cat_neighbors):
    """Show grid of images."""
    # holds an array column
    image_array = np.array(cat_neighbors)
    # new_image_table = cat_neighbors.unpack('image_array')
    # print new_image_table
    img_dat = dict()
    # for i, v in enumerate(cat_neighbors['image_array']):
    #     print '\n'   
    #     img_sarry = gl.SArray(v)
    #     print "img_arry is", img_sarry
    #     print '\n'
    #     img_dat[i] = img_sarry
    #     print '\n'
    cat_neighbors["image1"] = cat_neighbors['image_array'].pixel_array_to_image( 32, 32, 3, allow_rounding = True)
    images = cat_neighbors["image1"]

    return render_template("imagelist.html", images=images)

    # for i, v in enumerate(image_array):
    #     print '\n'   
    #     # b = v['image_array']
    #     # img_sarray = gl.SArray(b)
    #     # print img_sarray
    #     # print '\n'
    # print img_dat
    #     rslt_img_sarray = gl.SArray.pixel_array_to_image(img_sarray, 32, 32, 3, allow_rounding = True)
    #     print type(rslt_img_sarray)

        # The images are of size 32 x 32 x 3 (RGB channels)
        # (since they are RGB). Since the scaling will still result in some non-integer
        # values, we want to set allow_rounding to True.
        # rslt_img_sarray = gl.SArray.pixel_array_to_image(img_sarry, 32, 32, 3, allow_rounding = True)
        # print type(rslt_img_sarray)
    
    # print img_dat

    # print img_dat
    # print image_array
    # holds pixel data
    print "***********************"
    print '\n'
    a = np.array(cat_neighbors['image_array'])
    print "***********************"
    print '\n'
    # print cat_neighbors['id']
    # print cat_neighbors.filter_by('image_array')
    print '\n'
    # print "***********************"
    # print cat_neighbors['image_array']
    # print a

    # img = PIL.Image.fromarray(a)

    # # holds id of images
    # b = np.array(cat_neighbors['id'])
    # print b

    # print "image", len(image_array)
    print "cat neighbors: ",  len(cat_neighbors)
    # image_array = image_array.reshape(len(cat_neighbors), len(image_array))
    # print image_array

    # images = Image.query.all()
    # return render_template("image_list.html")

# def transform_to_pil(pix):
#     data = list(tuple(pixel) for pixel in pix)

@app.route('/cats')
def show_cats(image_train):
    """Show cat images."""

    cat = image_train[18:19]
    knn_model = graph_lab.knn_model_generic(image_train)
    cat_neighbors = graph_lab.get_images_from_ids(image_train, knn_model.query(cat))
    print cat_neighbors
    # cat_neighbors['image'].show()
    # image_list(cats)


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