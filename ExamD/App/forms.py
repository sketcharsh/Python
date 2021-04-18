from django.forms import ModelForm
from .models import Register
class FormReg(ModelForm):
	class Meta:
		model = Register
		fields = ['Name','Mail','Password']
