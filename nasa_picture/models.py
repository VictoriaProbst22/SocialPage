from datetime import date
from django.db import models

# Create your models here.
class Picture(models.Model):
    copyright = models.CharField(max_length=255)
    explanation = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField()