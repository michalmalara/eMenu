from django.db import models
from django.utils import timezone


# Create your models here.

class Menu(models.Model):
    name = models.TextField(max_length=50, unique=True)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
            On save, update timestamps
        """
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Menu, self).save(*args, **kwargs)
