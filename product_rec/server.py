""" Product Recommender """

# Author: Shai Wilson

from jinja2 import StrictUndefined

# from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import connect_to_db, db, Image, Tag, Image_Tags

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
    graph_lab.my_batch_job('seed_data/image_train_data/')
    return render_template("welcome.html")


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
@app.route("/update_tags", methods=['POST'])
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

@app.route("/images")
def image_list():
    """Show grid of images."""

    # images = Image.query.all()
    # return render_template("image_list.html", images=image)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()