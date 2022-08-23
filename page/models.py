from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    date = models.DateField()
    