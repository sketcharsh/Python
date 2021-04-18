from django.db import models

# Create your models here.
class RestDet(models.Model):
	RestName=models.CharField(max_length=100)
	RestId=models.IntegerField()