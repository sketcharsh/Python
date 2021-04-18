from django.db import models

# Create your models here.
class Cust(models.Model):
	CustName = models.CharField(max_length=200)
	CustId = models.IntegerField()
	def __str__(self):
		return self.CustName
