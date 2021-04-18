from django.forms import ModelForm
from .models import Registration

class FormReg(ModelForm):
	class Meta:
		model = Registration
		fields = ['Name','Mail','Password']