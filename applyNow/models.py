from django.db import models

class Apply(models.Model):
    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.TextField()