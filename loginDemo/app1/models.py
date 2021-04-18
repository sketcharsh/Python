from django.db import models

# Create your models here.

class User(models.Model):
	userId=models.IntegerField()
	userName=models.CharField(max_length=200)
	userPwd=models.CharField(max_length=200)

	def __str__(self):
		return str(self.userName)