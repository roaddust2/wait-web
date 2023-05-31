from io import BytesIO
from PIL import Image
from django.core.files import File


QUALITY = 40


def compress(image):
    """Simple function to compress image by QUALITY"""
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=QUALITY)
    new_image = File(im_io, name=image.name)
    return new_image
