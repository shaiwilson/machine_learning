# """Models and database functions for Product Recommender project."""
# Author : Shai Wilson

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

import graphlab as gl

# .show on a graphlab object returns a json object 

# load data set into SFRAMES

print "*********************"
print "Reading the data"
image_train=gl.SFrame('seed_data/image_train_data/')
image_test=gl.SFrame('seed_data/image_test_data/')
gl.canvas.set_target('browser', 5000)

print "*********************"
print "expecting 2005 images:", len(image_test)
print "*********************"

print "*********************"
print "training the model"
print image_train.head()
print "*********************"

# IMAGE CLASSIFICATION TASK
# Train a classifier on the raw image pixels using transfered learning
# deep_feautures already contains the pre-computed deep features for this data
# features = deep_features pretrained
# target = thing i'm trying to predict is given by the label column
# creating a classifier on 2000 images using features computed in 
# the neural network from: http://s3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45
# deep_features_model = gl.logistic_classifier.create(image_train,
#                                                          features=['deep_features'],
#                                                          target='label')

# IMAGE RETREVIAL TASK
# Create a nearest neighbors model for image retrieval 
# train nearest neighbors model for retrieving images using deep features
knn_model = graphlab.nearest_neighbors.create(image_train,features=['deep_features'],
                                             label='id')



print "Reading image_test and making predictions"
# apply the deep features model to the images that the user chooses
print "*********************"

# TODO
# covert the column tag_category to a dictionary


# ##############################################################################
# # Part 1: Models



# ##############################################################################
# # Helper functions

# Use image retrieval model with deep features to find similar images
# expecting : pair_of_images = image_train[image_id_1:image_id_2]
# neighbors = get_images_from_ids(knn.model.query(pair_of_images))
# neighbors['image'].show
def get_images_from_ids(query_result):
    return image_train.filter_by(query_result['reference_label'],'id')

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
