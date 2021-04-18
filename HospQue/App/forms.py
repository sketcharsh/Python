from django.forms import ModelForm
from .models import Doctor
class Login(ModelForm):
	class Meta:
		model = Doctor
		fields = ['DrName','DrAge']