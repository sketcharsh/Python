from django.db import models

# Create your models here.
class Book(models.Model):
	BookId = models.IntegerField()
	BookName = models.CharField(max_length=200)