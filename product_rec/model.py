# """Models and database functions for Product Recommender project."""
# Author : Shai Wilson

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

##############################################################################
# Model definitions


class Image(db.Model):
    """User of ratings website."""

    __tablename__ = "images"

    image_id = db.Column(db.Integer, primary_key=True)
    image_label = db.Column(db.String(64), nullable=False)
    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Image image_id=%s label=%s>" % (self.image_id, self.image_label)


class Label(db.Model):
    """Labels on images."""

    __tablename__ = "labels"

    label_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100))
    image_id = db.Column(db.Integer)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Label label_id=%s label_title=%s>" % (self.label_id, self.title)


class Rating(db.Model):
    """Rating of a movie by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>" % (
            self.rating_id, self.movie_id, self.user_id, self.score)

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///compvision'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
