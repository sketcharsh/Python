from django.forms import ModelForm
from .models import Signup
class SigForm(ModelForm):
	class Meta:
		model = Signup
		fields = ['Name','Mail','Password']
