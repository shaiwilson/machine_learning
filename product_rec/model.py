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

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tag_label = db.Column(db.String(64), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Tag tag_id=%s label=%s>" % (self.tag_id, self.tag_label)

class Image_Tags(db.Model):
    """Tags of an image by image."""

    __tablename__ = "imagetags"

    image_id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.Integer, nullable=False)

    # Define relationship to Images
    image = db.relationship("Image",
                            backref=db.backref("imagetags", order_by=tag_id))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Tag image_id=%s tag_id=%s>" % (self.iamge_id, self.tag_id)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///visuals'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

 
    from server import app
    connect_to_db(app)
    print "Connected to DB."
