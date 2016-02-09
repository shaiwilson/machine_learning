# """Models and database functions for Product Recommender project."""
# Author : Shai Wilson

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

import graphlab as gl

# .show on a graphlab object returns a json object 

# gl.canvas.set_target('browser', 5000)
# load data set into SFRAMES
# image_train=gl.SFrame('seed_data/image_train_data/')
# image_test=gl.SFrame('seed_data/image_test_data/')
# # image_train['image'].show()
# print "*********************"
# print "expect 2005:", len(image_test)
# convert to python object
# 

# ##############################################################################
# # Part 1: Data Visualization



# ##############################################################################
# # Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    # connect_to_db(app)
    print "Connected to DB."


# def connect_to_db(app):
#     """Connect the database to our Flask app."""

#     # Configure to use our SQLite database
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
#     app.config['SQLALCHEMY_ECHO'] = True
#     db.app = app
#     db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    # connect_to_db(app)
    # print "Connected to DB."
