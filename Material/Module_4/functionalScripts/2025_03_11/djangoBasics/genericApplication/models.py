from django.db import models

# Create your models here.
class Names (models.Model):
    firstname = models.CharField (max_length=100)