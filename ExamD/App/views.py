from django.shortcuts import render
from .models import Register
from .forms import FormReg
# Create your views here.
def signup(request):
	obj = FormReg()
	data = {'id':obj}
	return render(request,'App/register.html',data)

def insert(request):
	name = request.POST.get("Name")
	mail = request.POST.get("Mail")
	pwd = request.POST.get("Password")
	Register.objects.create(Name=name,Mail=mail,Password=pwd)
	return render(request,'App/Success.html')

	


















