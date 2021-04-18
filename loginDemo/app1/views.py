from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from .models import User


def index(request):
	return render(request,"app1/index.html")
	

def register(request):
	return render(request,"app1/register.html")

def registerAddUser(request):
	print("in method")
	unm = request.POST.get("username")
	pwd = request.POST.get("password")
	User.objects.create(userId=1,userName=unm,userPwd=pwd)
	return render(request,"app1/success.html")



def loginCheck(request):

	unm = request.POST.get("username")
	pwd = request.POST.get("password")

	if(unm=="GLS" and pwd=="12345"):
		lstUsrs = User.objects.all()
		dictUsers={"users":lstUsrs}
		request.session['Patwa']=unm
		return render(request,"app1/success.html",dictUsers)
	else:
		return render(request,"app1/failure.html")


def updateuser(request):
	v1=request.GET.get("name")

	list1=User.objects.all()

	checked=False

	for data in list1:
		if(v1==data.userName):
			obj=User.objects.get(userName=v1)


			checked=True

			data={'userId':data.userId,'userName':data.userName,'userPwd':data.userPwd}

			if(checked==True):
				return render(request,"app1/updatepage.html",data)
			else:
				return HttpResponse("Error in Update")


def updatedata(request):
	v1=request.POST.get("userId")
	v2=request.POST.get("userName")
	v3=request.POST.get("userPwd")

	list1=User.objects.all()

	checked=False

	for data in list1:
		print(data.userName)
		if(data.userName==v2):
			checked=True

	if(checked==True):
		u1 = User.objects.get(userName=v2)
		u1.userId=v1
		u1.userName=v2
		u1.userPwd=v3
		u1.save()
		return HttpResponse("update")
	else:
		return HttpResponse("Error in Update")

def deleteuser(request):
	v1=request.GET.get("name")

	list1=User.objects.all()

	checked=False

	for data in list1:
		if(v1==data.userName):
			d1=User.objects.filter(userName=v1)
			d1.delete()
			checked=True

			if(checked==True):
				return HttpResponse("delete")
			else:
				return HttpResponse("Error in Delete")


def logout(request):
	try:
		del request.session['Patwa']
	except:
		print("Error")
	return HttpResponse("logout")