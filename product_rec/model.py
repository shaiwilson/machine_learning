"""Models and database functions for Product Recommender project."""
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

class Tag(db.Model):
    """Association table for image tags."""

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer, primary_key=True)
    tag_label = db.Column(db.String(64), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Tag tag_id=%s label=%s>" % (self.tag_id, self.tag_label)

class Image_Tags(db.Model):
    """Model many-to-Many relationship between images and tags."""

    __tablename__ = "imagetags"

    image_id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Tag image_id=%s tag_id=%s>" % (self.iamge_id, self.tag_id)


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///visuals'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
