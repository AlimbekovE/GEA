from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    text = models.TextField()