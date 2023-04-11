from django.db import models


class CarouselItem(models.Model):
    """Carousel slide object to display on home page"""

    label = models.CharField('Label', max_length=255)
    placeholder = models.CharField('Placeholder', max_length=255)
    image = models.ImageField('Image', upload_to='static/images/carousel/')
    image_alt = models.CharField(
        'Image alternative text',
        max_length=255,
        null=True,
        blank=True,
    )
    priority = models.IntegerField('Priority', default=1)

    def __str__(self):
        return self.label
