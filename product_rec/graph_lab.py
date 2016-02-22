# Author : Shai Wilson

"""  

    Part I focuses on loading the data.

    Part II focuses on using a pre-trained neural net to extract visual features.

    Part III focuses on using the extracted visual features to train a nearest neighbors model.

"""

import graphlab as gl
from PIL import Image
from IPython.display import display
from IPython.display import Image


# ##############################################################################

# # Part 1: Read Data


def save_data(image_test):
	"""Save image_train data to csv"""

	# inspect the images in the data set
	print "*********************"
	print "expecting 4000 images:", len(image_test)
	print "*********************"


	# [column_names]
	# 0000=id
	# 0001=image
	# 0002=label
	# 0003=deep_features
	# 0004=image_array

	print "*********************"
	print "save image labels to csv"
	all_image_labels = image_test['label']
	image_labels = gl.SArray(all_image_labels)
	all_image_labels.save('all_image_labels.csv')
	print "*********************"
	all_image_ids = image_test['id'].astype(int)
	image_id = gl.SArray(all_image_ids)
	print "*********************"
	print "create a csv file concatenated with the id and label"
	image_id_and_label = gl.SFrame({'ids': image_id, 'label': image_labels})
	image_id_and_label.save('image_id_and_label.csv')
	print "*********************"

def clean_test_data(path):

	print "*********************"
	print "Reading the test data"

	image_test=gl.SFrame('seed_data/image_test_data/')
	return image_test

def clean_train_data(path):

	print "*********************"
	print "Reading the training data"

	image_train=gl.SFrame('seed_data/image_train_data/')
	return image_train


def setup_training(image_train):

	print "*********************"
	print "Given the deep features, train a classifier"
	deep_features_model = train_images(image_train)
	return deep_features_model


# ##############################################################################
# Part 2: Use a pre-trained Neural Network to train the images

def train_images(image_train):

		""" IMAGE CLASSIFICATION TASK
		Train a classifier on the raw image pixels using transfered learning
		deep_feautures already contains the pre-computed deep features for this data. """
		import graphlab as gl
		# features = deep_features pretrained
		# target = thing i'm trying to predict is given by the label column
		# creating a classifier on 4000 images using features computed in 
		# the neural network from: http://s3.amazonaws.com/GraphLab-Datasets/deeplearning/imagenet_model_iter45

		deep_features_model = gl.logistic_classifier.create(image_train,
		                                                         features=['deep_features'],
		                                                         target='label')
		return deep_features_model



# ##############################################################################
# Part 3: focuses on using the extracted visual features to train a nearest neighbors model.

# Overview:
# 	server.py obtain image_id from db from the image the user clicks
# 	sends image_id here to find the nearest neighbors
# 	apply the deep features model to the images that the user chooses.


def get_images_from_ids(image_train, query_result):

	"""	Use image retrieval model with deep features to find similar images
	expecting : pair_of_images = image_train[image_id_1:image_id_2]
	neighbors = get_images_from_ids(knn.model.query(pair_of_images))
	neighbors['image'].show """

	print "*********************"
	print "Reading in images and making predictions"
	print "*********************"

	return image_train.filter_by(query_result['reference_label'],'id')

# generic image retieval model

def my_batch_job(path_train):
	""" Load common image analysis data set"""
	print "Load common image analysis data set"

	image_train=gl.SFrame(path_train)
	return image_train

def image_model_generic(path_train):
	""" A simple image retrieval system that finds the nearest neighbors 
	for any image. """

	print "*********************"
	print "training nearest neighbors model"
	
	#  IMAGE RETREVIAL TASK
	# 	  Create a nearest neighbors model for image retrieval 
	# 	  train nearest neighbors model for retrieving images using deep features

	knn_generic_model = gl.nearest_neighbors.create(path_train,features=['deep_features'], label='id')
	return knn_generic_model	

# Category specific image retrieval models

def dog_category(image_train):
	""" Evaluates whether the image is similar enough to dog images """

	dog_model = gl.SFrame(image_train[image_train['label'] == 'dog'])
	knn_dog_model = gl.nearest_neighbors.create(dog_model,features=['deep_features'], label='dog')
	return knn_dog_model


def cat_category(image_train):
	""" Evaluates whether the image is similar enough to cat images """

	cat_model = gl.SFrame(image_train[image_train['label'] == 'cat']) 
	knn_cat_model = gl.nearest_neighbors.create(cat_model,features=['deep_features'], label='cat')
	return knn_cat_model

# A generic function to automate get_image_by_id based for 
# either a specific category or for a generic sampling
def model_query(model_type, label_type, knn_model):

	""" Return the query result for specific category of image.
	model_type = dog, cat, bird, auto
	label_type = cat, dog, unknown
	EX: cat_neighbors = get_images_from_ids(knn_model.query(cat)) """

	closest_neighbors = get_images_from_ids(model_type, knn_model.query(label_type))

	return closest_neighbors 

# ##############################################################################
# Part 4: Clustering

# Overview:
# 	server.py obtain image_id from db from the image the user clicks
# 	sends image_id here to find the nearest neighbors
# 	apply the deep features model to the images that the user chooses.


# ##############################################################################
# Part 5: 

# Overview:
# 	server.py obtain image_id from db from the image the user clicks
# 	sends image_id here to find the nearest neighbors
# 	apply the deep features model to the images that the user chooses.


# Show images
def show_graphlab_image(i, image_train):

    img = Image(filename=image_train['label'][i], width=100, height=100)
    display(img)

def show_images(image_train, field):
    for x in image_train:
        x = x[field] # i.e : cat
        print "id " + str(x) + " -> " + image_train['label'] + ":"
        # show_graphlab_image(image_train, x)




