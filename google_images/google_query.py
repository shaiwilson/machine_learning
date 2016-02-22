# Using Google images query searching for "Black Dress" ~ 100 images

import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError
from scipy.misc import imread
import graphlab as gl

size = 256,256

# print "hello, world."

def go(query, path):
  BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
             'v=1.0&q=' + query + '&start=%d'
  
  if not os.path.exists(path):
    os.makedirs(path)

    start = 0
      while start < 60:
        r = requests.get(BASE_URL % start)
        if json.loads(r.text)['responseData']['results'] is not None:
          for image_info in json.loads(r.text)['responseData']['results']:
            url = image_info['unescapedUrl']
            try:
              image_r = requests.get(url)
            except ConnectionError, e:
              print 'could not download %s' % url
              continue
            title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')
            file = open(os.path.join(path, '%s.jpg') % title, 'w')
            try:
              img = Image.open(StringIO(image_r.content))
              img.thumbnail(size, Image.ANTIALIAS)
              Image.open(StringIO(image_r.content)).save(file, 'JPEG')
              imread(file.name)
            except IOError, e:
              os.remove(file.name)
              continue
            finally:
              file.close()
          start += 4

def clean(path):
  i = 0
  for f in os.listdir(path):
    os.rename(path + '/' + f, path + '/' + str(i) + '.jpg')
    i += 1

 
go('barcelona building', 'images')
go('barcelona buildings', 'images')

clean('images')






