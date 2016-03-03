import wtforms

from model import Tag

class EntryForm(wtforms.Form):
    

    def save_entry(self, image):
        self.populate_obj(image)
        return image

class ImageForm(wtforms.Form):
    file = wtforms.FileField('Image file')