from django.shortcuts import render
from .models import Course
from .forms import Register
# Create your views here.
def index(request):
	return render(request,'App/index.html')
def login(request):
	obj = Register()
	data = {'id': obj}
	return render(request,'App/login.html',data)