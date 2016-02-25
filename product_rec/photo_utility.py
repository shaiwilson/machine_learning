# You need the following package for this
# Installation : pip install pillow
# Source : http://pillow.readthedocs.org/en/latest/index.html
import PIL.Image
import graphlab as gl
import StringIO as _StringIO
import graph_lab


_format = {'JPG': 0, 'PNG': 1, 'RAW': 2, 'UNDEFINED': 3}

def to_pil_image(gl_single):
    """
    Returns a PIL Image constructed from the passed graphlab.Image
    Parameters
    ----------
        gl_img : graphlab.Image
            A graphlab.Image that is to be converted to a PIL Image
    Returns
    -------
        out : PIL.Image
            The input converted to a PIL Image
    """
    # if gl_single._format_enum == _format['RAW']:
        # Read in Image, switch based on number of channels.
    if gl_single.channels == 1:
        img = PIL.Image.frombytes('L', (gl_single._width, gl_single._height), str(gl_img._image_data))
    elif gl_single.channels == 3:
        img = PIL.Image.frombytes('RGB', (gl_single._width, gl_single._height), str(gl_img._image_data))
    elif gl_single.channels == 4:
        img = PIL.Image.frombytes('RGBA', (gl_single._width, gl_single._height), str(gl_img._image_data))
    else:
        raise ValueError('Unsupported channel size: ' + str(gl_single.channels))
    # else:
    #     img = PIL.Image.open(_StringIO.StringIO(gl_single._image_data))

    gl_single.save('outfile' + '.jpg')


# Sample conversion
# gl_img = gl.Image('http://s3.amazonaws.com/gl-testdata/images/sample.jpg')
# # pil_img = to_pil_image(gl_img)

gl.canvas.set_target('browser')
image_train = graph_lab.my_batch_job('seed_data/image_train_data/')

# test a generic model for cats
knn_model = graph_lab.image_model_generic(image_train)
cat = image_train[19]
cat = [cat]
# cat_neighbors = graph_lab.get_images_from_ids(image_train, knn_model.query(cat))

# graph_lab.show_images(cat_neighbors, 'image') 
# cat_neighbors['image'].show()
pil_img = to_pil_image(cat)
print pil_img


