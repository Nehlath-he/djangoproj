from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    source=models.CharField(max_length=100)