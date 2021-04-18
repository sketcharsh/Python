from .forms import ModelForm
from .models import Cust
class Register(ModelForm):
	class meta:
		model = Cust
		fields=['CustName','CustId']