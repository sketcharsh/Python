from django.db import models

# Create your models here.
class Empl(models.Model):
	EId = models.IntegerField()
	EName = models.CharField(max_length=200)