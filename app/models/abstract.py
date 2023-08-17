from django.db import models
from utils.optimizer import compress


class AbstractCompressImage(models.Model):
    
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
