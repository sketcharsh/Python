from django.forms import ModelForm
from .models import Demo

class AddUsr(ModelForm):
	class Meta:
		model = Demo
		fields=['no','name']