
from django.db import models

# Create your models here.
class Demo(models.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=200)

	def __str__(self):
		return self.name

class User(models.Model):
	usn=models.CharField(max_length=200)
	psw=models.CharField(max_length=20)

	def __str__(self):
		return self.usn

