from django.shortcuts import render
from .forms import Register
from .models import Registration
# Create your views here.
def index(request):
	obj = Register()
	data = {'id': obj}
	return render(request,'App/index.html',data)