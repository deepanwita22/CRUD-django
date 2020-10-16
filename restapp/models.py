from django.db import models

# Create your models here.
class General_detail(models.Model):
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=60)
    image_url = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)