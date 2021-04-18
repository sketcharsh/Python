from django.db import models
# Create your models here.
class Registration(models.Model):
	fname = models.CharField(max_length=200)
	mail = models.CharField(max_length=200)
	psw = models.CharField(max_length=200)
