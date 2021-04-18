from django.shortcuts import render
from .forms import LoginD
from .models import RestDet
# Create your views here.
def index(request):
	return render(request,'App/index.html')
def login(request):
	obj = LoginD()
	data = {'id' : obj}
	return render(request,'App/login.html',data)