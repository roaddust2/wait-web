from django.db import models
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from app.models.abstract import AbstractImage


def carouselitem_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    path = "images/carousel/{0}.{1}".format(uuid4().hex, ext)
    return path


class CarouselItem(AbstractImage):
    """Carousel slide object to display on home page"""

    label = models.CharField(_('Label'), max_length=255)
    placeholder = models.CharField(_('Placeholder'), max_length=255, null=True, blank=True)
    text_color = models.CharField(_('TextColor'), max_length=255, null=True, blank=True)
    link = models.CharField(_('Link'), max_length=255, null=True, blank=True)
    image = models.ImageField(
        _('Image'),
        width_field='image_width',
        height_field='image_height',
        upload_to=carouselitem_directory_path
    )
    image_width = models.IntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)
    image_webp = models.ImageField(upload_to=carouselitem_directory_path, null=True, blank=True)
    image_alt = models.CharField(_('ImageAlt'), max_length=255, null=True, blank=True)
    priority = models.IntegerField(_('Priority'), default=1)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('CarouselItem')
        verbose_name_plural = _('CarouselItems')
