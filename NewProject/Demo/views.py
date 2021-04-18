from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def DemoView(request):
	# return HttpResponse("First Page")
	dict={
	'data':"Harsh",
	'que':"How are you?"
	}
	return render(request,'Demo/index.html',dict)
def second(request):
	# return HttpResponse("First Page")
	return render(request,'Demo/second.html')
def home(request):
	strUnm= request.POST.get('email')
	strPwd= request.POST.get('pw')
	lstUser=[]
	list1= User.objects.all()
	flag=False
	for singleUsr in list1:
		if(singleUsr.usn==strUnm and singleUsr.psw==strPwd):
			flag=True
	if(flag==True):
		return render(request,'Demo/success.html')
	else:
		return render(request,'Demo/fail.html')

	# if(models.usn==strUnm and models.psw==strPwd):
	# 	return HttpResponse("Success")
	# else:
	# 	return HttpResponse("Fail")
	# dict1={
	# 'u1':"Harsh",
	# 'pw1':"1234"
	# }
	# dict2={
	# 'u1':"GLS",
	# 'pw1':"123"
	# }
	# lstUser.append(dict1)
	# lstUser.append(dict2)
	# flag=False
	# for singleUsr in lstUser:
	# 	if(singleUsr["u1"]==strUnm and singleUsr["pw1"]==strPwd):
	# 		flag=True

	# if(flag==True):
	# 	return render(request,'Demo/success.html')
	# else:
	# 	return render(request,'Demo/fail.html')







			