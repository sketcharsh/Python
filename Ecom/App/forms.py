from django.forms import ModelForm
from .models import Register
from .models import Product
class RegForm(ModelForm):
	class Meta:
		model = Register
		fields = ['u_name','u_email','u_password']
class ProdForm(ModelForm):
	class Meta:
		model = Product
		fields = ['p_id','p_name','p_desc','c_obj']