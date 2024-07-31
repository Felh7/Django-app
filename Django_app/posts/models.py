from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class UserPost(models.Model):
    username = models.CharField(max_length=24)
    text = models.CharField(max_length=1024, blank=True)
    file = models.FileField(upload_to='upload', blank=True)
    def clean(self):
        if not (self.text or self.file):
            raise ValidationError("You must specify either text or file")
