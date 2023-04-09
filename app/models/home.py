from django.db import models


class CarouselItem(models.Model):
    label = models.CharField('Label', max_length=200)
    placeholder = models.CharField('Placeholder', max_length=600)
    image = models.ImageField('Image', upload_to='static/images/')
    image_alt = models.CharField(
        'Alternative text',
        max_length=200,
        null=True,
        blank=True,
    )
    priority = models.IntegerField('Priority', default=1)

    def __str__(self):
        return self.label
