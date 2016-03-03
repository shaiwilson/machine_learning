"""Models and database functions for Product Recommender project."""
# Author : Shai Wilson

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

##############################################################################
# Model definitions


image_tags = db.Table('image_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('image_id', db.Integer, db.ForeignKey('images.id'))
)

class Image(db.Model):
    """User of ratings website."""

    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image_label = db.Column(db.String(64), nullable=False) 

    tags = db.relationship('Tag', secondary=image_tags,
        backref=db.backref('images', lazy='dynamic'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Image image_id=%s label=%s>" % (self.id, self.image_label)

class Tag(db.Model):
    """Association table for image tags."""

    __tablename__ = "tag"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Tag tag_id=%s label=%s>" % (self.id, self.name)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///visuals'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

 
    from server import app
    connect_to_db(app)
    print "Connected to DB."
