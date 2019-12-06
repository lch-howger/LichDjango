from django.db import models


# Create your models here.
class Star(models.Model):
    id = models.TextField(primary_key=True)
    star = models.TextField()
    time = models.TextField()
    text = models.TextField(max_length=None)
