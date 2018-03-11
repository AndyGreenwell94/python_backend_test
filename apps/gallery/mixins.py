from .models import Image


class ImageRelationMixin(object):

    @property
    def images(self):
        return Image.objects.get_for_object(self)
