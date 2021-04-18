from django.shortcuts import render
from .forms import Login
# Create your views here.
def index(request):
	return render(request,'App/index.html')
def login(request):
	obj = Login()
	data = {'id': obj}
	return render(request,'App/login.html',data)