import re
import uuid

from io import BytesIO
# from PIL import Image
from django.core.files import File


# image compression method
from django.utils.text import slugify


# def compress(image):
#     im = Image.open(image)
#     im_io = BytesIO()
#     im.save(im_io, 'JPEG', quality=60)
#     new_image = File(im_io, name=image.name)
#     return new_image
#
#
# class MetaMixin:
#     """A mixin that can be used to render a template."""
#     meta_title = None
#     meta_description = None
#
#
def _delete_articles(value):
    """
    Substitute the articles with a space and return the word
    """
    return re.sub('(\s+)(e|il|lo|la|i|gli|le)(\s+)', ' ', value)


def create_slug(value, add_uuid=True, remove_articles=True):
    if remove_articles:
        value = _delete_articles(value)
    if add_uuid:
        rnd_str = str(uuid.uuid4())[:8]
        return slugify(value) + '-' + rnd_str
    return slugify(value)
