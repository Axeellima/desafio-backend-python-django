from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=25)
    nature = models.CharField(max_length=10)
