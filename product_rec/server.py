""" Product Recommender """

# Author: Shai Wilson

from jinja2 import StrictUndefined

# from flask_debugtoolbar import DebugToolbarExtension

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import connect_to_db, db, Image

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
    graph_lab.my_batch_job('seed_data/image_train_data/')
    return render_template("welcome.html")


@app.route('/')
def index():
    """Homepage."""
    gl.canvas.set_target('browser')
    return render_template("homepage.html")

@app.route('/search', methods=['GET'])
def search_db():
    """Search page."""

    text_query = request.args.get["query"]
    print text_query

    # image_ids = Image.query.filter_by(image_label=text_query).all()


    # return render_template("results.html")

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