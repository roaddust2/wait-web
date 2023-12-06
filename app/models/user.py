from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
