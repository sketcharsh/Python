from django.shortcuts import render
from .forms import EmplLogin
from .models import Empl
# Create your views here.
def index(request):
	return render(request,'App/index.html')
def login(request):
	obj = EmplLogin()
	data = {'id' : obj}
	return render(request,'App/login.html',data)