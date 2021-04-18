from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse 
from .models import RegisterDetail
from .forms import Registration
# Create your views here.
def index(request):
	return render(request,'App/index.html')
def home(request):
	strUnm= request.POST.get('email')
	strPwd= request.POST.get('pw')
	lstUser=[]
	list1= RegisterDetail.objects.all()
	flag=False
	if(strUnm=='admin' and strPwd=='admin'):
		obj = RegisterDetail.objects.all()
		data = {"users": obj}
		return render(request,'App/Users.html',data)
	for singleUsr in list1:
		if(singleUsr.usrEm==strUnm and singleUsr.usrPs==strPwd):
			flag=True
	if(flag==True):
		request.session['name']=strUnm
		obj = RegisterDetail.objects.all()
		obj = RegisterDetail.objects.filter(usrEm=strUnm)
		data = {"users": obj}
		# for usrData in list1:
		# 	data = {'fn':usrData.usrFn,'ln':usrData.usrLn,'ph':usrData.usrPh,'em':usrData.usrEm}
		return render(request,'App/UserDetails.html',data)
	else:
		return render(request,'App/fail.html')
def JsonData(request):
	lstUser= list(RegisterDetail.objects.values())
	return JsonResponse(lstUser,safe=False)
def loginDetails(request):
	fn=request.POST.get("selectedUser")
	list1= RegisterDetail.objects.all()
	list1= RegisterDetail.objects.filter(usrFn=fn)
	# data={}
	# for usrData in list1:
	# 	if(fn==usrData.usrFn):
	# 		data={'fn':usrData.usrFn,'ln':usrData.usrLn,'ph':usrData.usrPh,'em':usrData.usrEm}
	# obj = RegisterDetail.objects.all()
	data = {"users": list1}
	return render(request,'App/UserDetails.html',data)
def Register(request):
	obj = Registration()
	data = {'id' : obj}
	return render(request,'App/Registration.html',data)
def insData(request):
	fn=request.POST.get("usrFn")
	ln=request.POST.get("usrLn")
	psw=request.POST.get("usrPs")
	ph=request.POST.get("usrPh")
	em=request.POST.get("usrEm")
	RegisterDetail.objects.create(usrFn=fn,usrLn=ln,usrPs=psw,usrPh=ph,usrEm=em)
	return render(request,'App/Success.html')
def Users(request):
	obj = RegisterDetail.objects.all()
	data = {"users": obj}
	return render(request,'App/Users.html',data)
def delete(request):
	fn=request.POST.get('selectedUser')
	print(fn)
	# obj = RegisterDetail.objects.all()
	obj= RegisterDetail.objects.filter(usrFn=fn)
	obj.delete()
	return HttpResponse("DELETED")
def update(request):
	print("in update")
	selectedUser = request.POST.get('selectedUser')
	# print(selectedUser)
	# sUsr=request.POST.get('selectedUser')
	fn=request.POST.get("fn")
	ln=request.POST.get("ln")
	psw=request.POST.get("ps")
	ph=request.POST.get("ph")
	em=request.POST.get("em")
	print(fn)
	obj = RegisterDetail.objects.get(usrFn=selectedUser)
	obj.usrFn=fn
	obj.usrLn=ln
	obj.usrPs=psw
	obj.usrPh=ph
	obj.usrEm=em
	obj.save()
	return HttpResponse("update")
	# data={'fn':obj.usrFn,'ln':obj.usrLn,'ps':obj.usrPs,'ph':obj.usrPh,'em':obj.usrEm}
	# dic ={'users':data}
	# return render(request,'App/Users.html',dic)
def logout(request):
	try:
		del request.session['name']
	except:
		pass
	return render(request,'App/index.html')