from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class places(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()


    def __str__(self):
        return self.name


class meet(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    descr=models.CharField(max_length=500)

    def __str__(self) :

        return self.name
