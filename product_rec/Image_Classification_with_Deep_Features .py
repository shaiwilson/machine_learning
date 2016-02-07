
# coding: utf-8

# In[1]:

import graphlab


# In[3]:

# Load a common image analysis dataset


# In[4]:

image_train = graphlab.SFrame('image_train_data/')
image_test = graphlab.SFrame('image_test_data/')


# In[5]:

image_train = graphlab.SFrame('image_train_data/')
image_test = graphlab.SFrame('image_test_data/')


# In[6]:

graphlab.canvas.set_target('ipynb')


# In[7]:

image_train['image'].show()


# In[10]:

#Train a classifier on the raw image pixels 


# In[12]:

raw_pixel_model = graphlab.logistic_classifier.create(image_train, target='label', 
                                              features=['image_array'])


# In[13]:

# Make a prediction with the simple model based on raw pixels


# In[14]:

image_test[0:3]['image'].show()


# In[15]:

image_test[0:3]['label']


# In[16]:

raw_pixel_model.predict(image_test[0:3])


# In[ ]:

raw_pixel_model = graphlab.logistic_classifier.create(image_train, target='label', 
                                              features=['image_array'])


# In[ ]:



