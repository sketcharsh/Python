from django.forms import ModelForm
from .models import Book
class Login(ModelForm):
	class Meta:
		model = Book
		fields = ['BookId','BookName']