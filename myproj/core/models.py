from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PhotoData(models.Model):
    photo = models.ImageField(upload_to='images/')
    time = models.DateTimeField()
    userId = models.IntegerField()

    def __str__(self):
        return str(self.userId)

