from django.forms import ModelForm
from .models import Empl
class EmplLogin(ModelForm):
	class Meta:
		model = Empl
		fields = ['EId','EName']