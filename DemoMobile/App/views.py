from django.shortcuts import render
from .models import Registration
from .forms import FormReg

# Create your views here.

def form(request):
	obj = FormReg()
	data = {'id':obj}
	return render(request,'App/Signup.html',data)

def insert(request):
	nm = request.POST.get("Name")
	em = request.POST.get("Mail")
	ps = request.POST.get("Password")
	Registration.objects.create(Name=nm,Mail=em,Password=ps)
	return render(request,'App/Success.html')

def loginPage(request):
	return render(request,'App/Login.html')

def login(request):
	em = request.POST.get("mail")
	ps = request.POST.get("pwd")
	lst = Registration.objects.all()
	flag=False

	for singleUser in lst:
		if(singleUser.Mail==em and singleUser.Password==ps):
			flag=True

	if(flag==True):
		return render(request,'App/Success.html')

	else:
		return render(request,'App/Fail.html')

	# em = request.POST.get("mail")
	# ps = request.POST.get("pwd")	
	# if(em=="Kiran" and ps=="123"):
	# 	return render(request,'App/Success.html')

	# else:
	# 	return render(request,'App/Fail.html')
	

def details(request):
	obj = Registration.objects.all()
	data = {'users':obj}
	return render(request,'App/UserDetails.html',data)
