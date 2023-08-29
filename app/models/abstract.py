from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from pathlib import Path


def convert_to_webp(image):
    """Convert image to webp"""

    name = str(Path(image.name).with_suffix('.webp'))
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, "webp", optimize=True, quality=70)
    new_image = File(im_io, name=name)
    return new_image


class AbstractImage(models.Model):

    def save(self, *args, **kwargs):
        self.image_webp = convert_to_webp(self.image)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
