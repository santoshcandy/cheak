from django.db import models

class Plumber(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=12)
    Phone = models.CharField(max_length=15)
    Service = models.TextField()
# Create your models here.
