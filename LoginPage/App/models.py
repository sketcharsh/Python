from django.db import models

# Create your models here.
class RegisterDetail(models.Model):
	usrFn=models.CharField(max_length=200)
	usrLn=models.CharField(max_length=200)
	usrPs=models.CharField(max_length=200)
	usrPh=models.IntegerField()
	usrEm=models.CharField(max_length=200)
	def __str__(self):
		return(self.usrFn)