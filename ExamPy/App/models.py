from django.db import models

# Create your models here.
class Signup(models.Model):
	Name = models.CharField(max_length=200)
	Mail = models.CharField(max_length=200)
	Password = models.CharField(max_length=200)