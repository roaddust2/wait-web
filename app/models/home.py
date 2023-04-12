from django.db import models
from django.utils.translation import gettext_lazy as _


class CarouselItem(models.Model):
    """Carousel slide object to display on home page"""

    label = models.CharField(_('Label'), max_length=255)
    placeholder = models.CharField(_('Placeholder'), max_length=255)
    image = models.ImageField(_('Image'), upload_to='static/images/carousel/')
    image_alt = models.CharField(_('ImageAlt'), max_length=255, null=True, blank=True)
    priority = models.IntegerField(_('Priority'), default=1)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('CarouselItem')
        verbose_name_plural = _('CarouselItems')