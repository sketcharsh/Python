from django.shortcuts import render
from .forms import SigForm
from .models import Signup
from django.http import JsonResponse
# Create your views here.
def Register(request):
	obj = SigForm()
	data = {'id':obj}
	return render(request,'App/register.html',data)
def Insert(request):
	nm = request.POST.get('Name')
	em = request.POST.get('Mail')
	ps = request.POST.get('Password')
	obj = Signup.objects.create(Name=nm,Mail=em,Password=ps)
	return render(request,'App/success.html')
def LoginPage(request):
	return render(request,'App/login.html')
def Login(request):
	email = request.POST.get('em')
	password = request.POST.get('ps')
	if(email=="GLS" and password=="123"):
		request.session['ssn']=email
		return render(request,'App/success.html')
	else:
		return render(request,'App/fail.html')
def UserDetails(request):
	obj = Signup.objects.all()
	data = {'id':obj}
	return render(request,'App/UserDetails.html',data)
def ViewDet(request):
	sel = request.POST.get('selected')
	# print(sel)
	obj = Signup.objects.filter(Name=sel)
	data = {'id':obj}
	return render(request,'App/ViewDetails.html',data)
def Update(request):
	sel = request.POST.get('selected')
	nm = request.POST.get('nm')
	em = request.POST.get('em')
	ps = request.POST.get('ps')
	obj = Signup.objects.get(Name=sel)
	obj.Name = nm
	obj.Mail = em
	obj.Password = ps
	obj.save()
	obj2 = Signup.objects.filter(Name=sel)
	data = {'id':obj2}
	return render(request,'App/ViewDetails.html',data)
def Delete(request):
	sel = request.POST.get('selected')
	obj = Signup.objects.filter(Name=sel)
	obj.delete()
	return render(request,'App/success.html')

def JsonData(request):
	lstUser = list(Signup.objects.values())
	return JsonResponse(lstUser,safe=False)