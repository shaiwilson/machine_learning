# Author : Shai Wilson

"""  

    Part I focuses on loading the data.

    Part II focuses on using a pre-trained neural net to extract visual features.

    Part III focuses on using the extracted visual features to train a nearest neighbors model.

"""

import graphlab as gl


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

# the data set contains some repeated labels, for instance, cat, dogs
# use the deduplication toolkit to remove copies
# how it works: injests data from SFrames and assigns and entity label to each row

def read_data(image_test):

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
	all_image_ids = image_test['id']
	image_id = gl.SArray(all_image_ids)
	print "*********************"
	print "create a csv file concatenated with the id and label"
	image_id_and_label = gl.SFrame({'ids': image_id, 'label': image_labels})
	image_id_and_label.save('image_id_and_label.csv')
	print "*********************"


# ##############################################################################
# Part 2: Use a pre-trained Neural Network to train the images

def train_images(image_train):

		""" IMAGE CLASSIFICATION TASK
		Train a classifier on the raw image pixels using transfered learning
		deep_feautures already contains the pre-computed deep features for this data. """

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


def image_retrieval(images):

	""" IMAGE RETREVIAL TASK
	  Create a nearest neighbors model for image retrieval 
	  train nearest neighbors model for retrieving images using deep features"""

	knn_model = gl.nearest_neighbors.create(image_train,features=['deep_features'], label='id')
	return knn_model


def get_images_from_ids(query_result):

	"""	Use image retrieval model with deep features to find similar images
	expecting : pair_of_images = image_train[image_id_1:image_id_2]
	neighbors = get_images_from_ids(knn.model.query(pair_of_images))
	neighbors['image'].show """

	print "*********************"
	print "Reading in images and making predictions"
	print "*********************"

	return # image_train.filter_by(query_result['reference_label'],'id')

# if __name__ == "__main__":

print "*********************"
print "Reading the data"

image_train=gl.SFrame('seed_data/image_train_data/')
image_test=gl.SFrame('seed_data/image_test_data/')

print "*********************"
print "training the model with imagenet"
# deep_features_model = train_images(image_train)
print "*********************"
print "training deep features model"
# knn_model = image_retrieval(image_train)
print "*********************"


