from django.db import models

# Create your models here.
class Doctor(models.Model):
	DrName = models.CharField(max_length=200)
	DrAge = models.IntegerField()
	# def __str__(self):
	# 	return self.DrName