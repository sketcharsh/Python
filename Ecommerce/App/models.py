from django.db import models

# Create your models here.
class Category(models.Model):
	c_obj = models.CharField(max_length=200)
	c_name = models.CharField(max_length=200)
	def __str__(self):
		return self.c_name
class Product(models.Model):
	p_id = models.CharField(max_length=200)
	p_name = models.CharField(max_length=200)
	p_desc = models.CharField(max_length=200)
	c_obj = models.ForeignKey('Category',on_delete=models.CASCADE)
	def __str__(self):
		return self.p_name
class Register(models.Model):
	u_name = models.CharField(max_length=200)
	u_email = models.CharField(max_length=200)
	u_password = models.CharField(max_length=200)
	def __str__(self):
		return self.u_name
class Carts(models.Model):
	ses_em = models.CharField(max_length=200)
	crt_id = models.CharField(max_length=200)
	crt_name = models.CharField(max_length=200)
	crt_desc = models.CharField(max_length=200)
	crt_qty = models.IntegerField(default=1)
	def __str__(self):
		return self.crt_name
	
