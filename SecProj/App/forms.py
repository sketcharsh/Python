from django.forms import ModelForm
from .models import Course
class Register(ModelForm):
	class Meta:
		model = Course
		fields = ['cName','cId']