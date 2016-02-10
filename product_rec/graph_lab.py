# Author : Shai Wilson
""" Read seed_data and train images """

import graphlab as gl
gl.canvas.set_target('browser')

# .show on a graphlab object returns a json object 
#
# [column_names]
# 0000=id
# 0001=image
# 0002=label
# 0003=deep_features
# 0004=image_array


# TODO
# covert the column tag_category to a dictionary
# add image id to database

# ##############################################################################
# # Part 1: Read Data


"""Loads data set into SFRAMES

	IMAGE CLASSIFICATION TASK
	Train a classifier on the raw image pixels using transfered learning
	deep_feautures already contains the pre-computed deep features for this data. """

print "*********************"
print "Reading the data"

image_train=gl.SFrame('seed_data/image_train_data/')
image_test=gl.SFrame('seed_data/image_test_data/')

print "*********************"
for i in range(20):
	print image_train['id']
print "*********************"

print "*********************"
print "expecting 4000 images:", len(image_test)
print "*********************"

print "*********************"
print "training the model"
print image_train.head()
print "*********************"


# features = deep_features pretrained
# target = thing i'm trying to predict is given by the label column
# creating a classifier on 4000 images using features computed in 
# the neural network from: http://s3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45
# deep_features_model = gl.logistic_classifier.create(image_train,
#                                                          features=['deep_features'],
#                                                          target='label')

# def image_retrieval(images):
# 	""" IMAGE RETREVIAL TASK
# 	    Create a nearest neighbors model for image retrieval 
# 	    train nearest neighbors model for retrieving images using deep features"""

#     	knn_model = gl.nearest_neighbors.create(image_train,features=['deep_features'], label='id')


# ##############################################################################
# # Helper functions

# Overview:
# server.py obtains image id from db, user clicks
# sends it here to find the nearest neighbors
# apply the deep features model to the images that the user chooses

# def get_images_from_ids(query_result):
# 	"""	Use image retrieval model with deep features to find similar images
# 	expecting : pair_of_images = image_train[image_id_1:image_id_2]
# 	neighbors = get_images_from_ids(knn.model.query(pair_of_images))
# 	neighbors['image'].show """

# 	print "*********************"
# 	print "Reading in images and making predictions"
# 	print "*********************"

#     return image_train.filter_by(query_result['reference_label'],'id')
















