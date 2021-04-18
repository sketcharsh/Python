from django.forms import ModelForm
from .models import RestDet
class LoginD(ModelForm):
	class Meta:
		model = RestDet
		fields = ['RestName','RestId']
