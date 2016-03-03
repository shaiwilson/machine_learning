from models import Tag

class ImageForm(wtforms.Form):
    file = wtforms.FileField('Image file')