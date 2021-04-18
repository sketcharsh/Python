from django.shortcuts import render
from django.shortcuts import redirect
from .models import Register
from .models import Category
from .models import Product
from .models import Carts
from .forms import RegForm
from .forms import ProdForm
# Create your views here.
def index(request):
	return render(request,'App/index.html')
def signup(request):
	obj = RegForm()
	data = {'id':obj}
	return render(request,'App/signup.html',data)
def insert(request):
	un = request.POST.get('u_name')
	em = request.POST.get('u_email')
	ps = request.POST.get('u_password')
	Register.objects.create(u_name=un,u_email=em,u_password=ps)
	obj = Category.objects.all()
	data = {'id':obj}
	request.session['ssn']=em
	return render(request,'App/category.html',data,em)
def loginPage(request):
	return render(request,'App/login.html')
def login(request):
	em = request.POST.get('email')
	ps = request.POST.get('password')
	lst = Register.objects.all()
	if(em=="admin" and ps=="admin"):
		return redirect('http://127.0.0.1:8000/admin/')
	flag = False
	for singleUsr in lst:
		if(em==singleUsr.u_email and ps==singleUsr.u_password):
			flag = True
	if(flag==True):
		obj = Category.objects.all()
		data = {'id':obj}
		request.session['ssn']=em
		return render(request,'App/category.html',data,em)
	else:
		return render(request,'App/fail.html')
def cat(request):
	# em = request.POST.get('email')
	# em = request.session['ssn']
	# print(em)
	obj = Category.objects.all()
	data = {'id':obj}
	return render(request,'App/category.html',data)
def prod(request):
	# em = request.session['ssn']
	# print(em)
	slprod = request.POST.get('selectedCat')
	lst = Product.objects.all()
	lst =  Product.objects.filter(c_obj=slprod)
	data = {'products':lst}
	return render(request,'App/product.html',data)
def ProdDetails(request):
	em = request.session['ssn']
	obj = ProdForm()
	data = {'id':obj}
	return render(request,'App/addprod.html',data)
def AddProd(request):
	try:
		em = request.session['ssn']
		print(em)
		ses = request.POST.get('ssn')
		pid = request.POST.get('pid')
		pnm = request.POST.get('nm')
		pdc = request.POST.get('desc')
		obj = Carts.objects.all()
		Carts.objects.create(ses_em=ses,crt_id=pid,crt_name=pnm,crt_desc=pdc)
		obj= Carts.objects.filter(ses_em=em)
		data = {'id':obj}
		return render(request,'App/mycart.html',data)
	except:
		return render(request,'App/login.html')
def Mycart(request):
	try:
		em = request.session['ssn']
		print(em)
		obj= Carts.objects.all()
		obj= Carts.objects.filter(ses_em=em)
		data = {'id':obj}
		return render(request,'App/mycart.html',data)
	except:
		return render(request,'App/login.html')
def Delete(request):
	em = request.session['ssn']
	pid = request.POST.get('pid')
	obj= Carts.objects.filter(crt_id=pid)
	obj.delete()
	em = request.session['ssn']
	obj2= Carts.objects.filter(ses_em=em)
	data = {'id':obj2}
	return render(request,'App/mycart.html',data)
def logout(request):
	try:
		del request.session['ssn']
	except:
		pass
	return render(request,'App/index.html')