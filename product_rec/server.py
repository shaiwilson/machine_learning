""" Product Recommender """

# Author: Shai Wilson

from jinja2 import StrictUndefined

# from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, render_template, redirect, request, flash, session, jsonify

import graphlab as gl
import graph_lab

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

# IMAGES = [
#     { "id": 1, "url": "http://unsplash.it/320/200"},
#     { "id": 2, "url": "http://unsplash.it/300/200"},
#     { "id": 3, "url": "http://unsplash.it/290/200"},
#     { "id": 4, "url": "http://unsplash.it/350/200"},
#     { "id": 5, "url": "http://unsplash.it/380/200"},
#     { "id": 6, "url": "http://unsplash.it/360/200"},
#     { "id": 7, "url": "http://unsplash.it/380/200"},
#     { "id": 8, "url": "http://unsplash.it/320/200"},
#     { "id": 9, "url": "http://unsplash.it/300/200"},
#     { "id": 10, "url": "http://unsplash.it/290/200"},
#     { "id": 11, "url": "http://unsplash.it/350/200"},
#     { "id": 12, "url": "http://unsplash.it/360/200"}
# ]

@app.route('/welcome')
def train():
    """Train image data."""
    graph_lab.my_batch_job('seed_data/image_train_data/')
    # return render_template("homepage.html", images=IMAGES)


@app.route('/')
def index():
    """Homepage."""
    gl.canvas.set_target('browser')
    # return render_template("homepage.html", images=IMAGES)

@app.route("/add-to-favorites", methods=["POST"])
def add_to_favorites():

    photo_id = request.form.get("id")

    # put this in a "favorites" table?

    return jsonify(status="success", id=photo_id)


@app.route("/images")
def image_list():
    """Show grid of images."""

    # images = Image.query.all()
    # return render_template("image_list.html", images=image)

# @app.route("/add-to-favorites", methods=["POST"])
# def add_to_favorites():

#     photo_id = request.form.get("id")

#     # put this in a "favorites" table?

#     return jsonify(status="success", id=photo_id)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True
    # visuals.connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()