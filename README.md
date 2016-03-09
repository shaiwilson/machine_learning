## Synopsis

Inspired by deep learning, View is an application that uses image pixel data in photos -- a subset of computer vision -- to identify visual characteristics.

When shown a photo of a flower, for example, the software responds with a group of like images. The software can predict the description of the image by identifying single objects. 

View uses a large collection of data from the imagenet competition to simulate a neural network for processing incoming data. The rules are simple, search by text or image and view provides you with images within the same classification. Users can also contribute by tagging images to help enhance the image search process.

## Tech Stack
Python, Graph Lab Create, Pillow, PostgreSQL, Numpy, Flask, Jinja

## Installation

Add Graph Lab Create to your virtualenv:

```python
pip install --upgrade --no-cache-dir https://get.dato.com/GraphLab-Create/1.8.3/your registered email address here/your product key here/GraphLab-Create-License.tar.gz
```

Run the following commands to set up the database:

```console
psql createdb visuals
```

```console
python -i model.py
db.create_all()
```

```console
python seed.py
```

Run the server:

```console
python server.py
```

You have to be sure that you added a licensed copy of [Graph Lab Create](https://dato.com/download/install-graphlab-create-command-line.html)

