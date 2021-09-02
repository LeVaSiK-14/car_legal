from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=127, default='')

class Mark(models.Model):
    bramd = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='marks')
    name = models.CharField(max_length=127, default='')