from django.forms import ModelForm
from .models import RegisterDetail
class Registration(ModelForm):
	class Meta:
		model = RegisterDetail
		fields = ['usrFn','usrLn','usrPs','usrPh','usrEm']