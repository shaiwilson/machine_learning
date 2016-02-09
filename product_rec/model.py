# """Models and database functions for Product Recommender project."""

# # Author : Shai Wilson

# from flask_sqlalchemy import SQLAlchemy

# # Here's where we create the idea of our database. We're getting this through
# # the Flask-SQLAlchemy library. On db, we can find the `session`
# # object, where we do most of our interactions (like committing, etc.)

# db = SQLAlchemy()

import graphlab as gl

# load data set
image_train=graphlab.SFrame('seed_data/image_train_data/')
image_test=graphlab.SFrame('seed_data/image_test_data/')

graphlab.canvas.set_target('browser')
image_train['image'].show()

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
