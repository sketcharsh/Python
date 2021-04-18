from django.forms import ModelForm
from .models import Registration
class Register(ModelForm):
	class Meta:
		model = Registration
		fields = ['fname','mail','psw']