from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Receipe(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='uploads/')
    category = models.CharField(max_length = 255)
    label = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    top = models.IntegerField()
    favourite = models.BooleanField()
    ingredients = ArrayField(models.CharField(max_length=200), blank=True)
    preparation = models.TextField()
