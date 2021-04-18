from django.db import models

# Create your models here.
class Student(models.Model):
	StuName = models.CharField(max_length=200)
	StuMarks = models.IntegerField()
	def __str__(self):
		return self.StuName
class Course(models.Model):
	cName = models.CharField(max_length=200)
	cId = models.IntegerField()
	def __str__(self):
		return self.cId