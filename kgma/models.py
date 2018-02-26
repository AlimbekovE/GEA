from django.db import models

class Kgma(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    text = models.TextField()