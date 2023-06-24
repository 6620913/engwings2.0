from distutils.command.upload import upload
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Videos(models.Model):
    course_id = models.IntegerField()
    cvs = models.IntegerField()
    thumbnail = models.ImageField(upload_to="pics")
    title = models.CharField(max_length=200)
    video =models.FileField(upload_to="wings/%y")
    udate =models.CharField(max_length=100)
    disc  =models.TextField()

    def __str__(self):
        return self.title
class Courses(models.Model):
    course_id = models.IntegerField()
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="pics")
    disc = models.TextField()
    def __str__(self):
        return self.name
