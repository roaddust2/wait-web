from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from pathlib import Path


JPEG_QUALITY = 40
WEBP_QUALITY = 70


def compress_image(image):
    """Compress image"""

    suffix = Path(image.file.name).suffix
    if suffix in {".jpeg", ".jpg"}:
        im = Image.open(image)
        im_io = BytesIO()
        im.save(im_io, "JPEG", quality=JPEG_QUALITY)
        new_image = File(im_io, name=image.name)
        return new_image

    else:
        return image


# def convert_to_webp(image):
#     """Convert image to webp"""

#     suffix = Path(image.file.name).suffix
#     if suffix == ".webp":
#         return image

#     name = str(Path(image.name).with_suffix('.webp'))
#     im = Image.open(image)
#     im_io = BytesIO()
#     im.save(im_io, 'webp', optimize=True, quality=WEBP_QUALITY)
#     new_image = File(im_io, name=name)
#     return new_image


class AbstractImage(models.Model):

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
