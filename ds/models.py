from django.db import models

# Create your models here.
class Tobacco(models.Model):
    tobacco_name = models.CharField(max_length=255)
    tobacco_rating = models.IntegerField(default=0, null=True)