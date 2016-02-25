""" Product Recommender """

# Author: Shai Wilson

from jinja2 import StrictUndefined

# from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import connect_to_db, db, Image, Tag, Image_Tags
from array import array
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


    # after search query returns images send to show page
    image_list(cat_neighbors)
    

    print "**********************"
    return render_template("welcome.html")


# what do u do when the dictionary key is a tuple, first item 
# is a string and the second item is a list of ints

@app.route("/images")
def image_list(cat_neighbors):
    """Show grid of images."""
    image_array = np.array(cat_neighbors)
    # result_array = np.empty((0, 100))
    img_dat = dict()
    for i, v in enumerate(cat_neighbors['image_array']):
         img_dat[i] = v[1:]

    print img_dat
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

    print "image", len(image_array)
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