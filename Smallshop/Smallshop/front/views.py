#coding:utf-8
from django.shortcuts import render,redirect
from django.http import request,JsonResponse
from forms import Frontuser_login,Frontuser_reg
from utils import login,logout
from decorators import front_login_required
from hashs import make_password
from models import FrontUser
from backstage.models import Commodity,ShoppingCart
from django.db.models import Q
import configs
# Create your views here.
def front_register(request):
	if request.method == 'GET':
		return render(request,'register.html')
	else:
		frontReg_form = Frontuser_reg(request.POST)
		if frontReg_form.is_valid():
			name = frontReg_form.cleaned_data.get('username',None)
			email = frontReg_form.cleaned_data.get('email',None)
			username = frontReg_form.cleaned_data.get('username',None)
			password = frontReg_form.cleaned_data.get('password',None)
			address = frontReg_form.cleaned_data.get('address',None)
			frontUser = FrontUser(name=name,
								  email=email,
								  username=username,
								  password=password,
								  address=address)
			frontUser.save()
			return JsonResponse({'code':200})
		else:
			return JsonResponse({'error':frontReg_form.errors})

def front_login(request):
	if request.method == 'GET':
		return render(request,'html')
	else:
		frontUser_form = Frontuser_login(request.POST)
		if frontUser_form.is_valid():
			username = frontUser_form.cleaned_data.get('username',None)
			password = frontUser_form.cleaned_data.get('password',None)
			if login(request,username,password):
				return JsonResponse({'message':u'登陆成功'})
			else:
				return JsonResponse({'error':u'用户名或密码错误'})
		else:
			return JsonResponse({'error':'用户名或密码格式不正确'})


@front_login_required
def front_logout(request):
	logout(request)
	return redirect('login.html')

@front_login_required
def shopCart(request,commodityId):
	if request.method == 'GET':
		userId = request.session[configs.LOGINED_KEY]
		shopcart = ShoppingCart.objects.filter(Q(user=userId)&Q(commodity=commodityId))
		

		return render(request,'shopCart.html')
	else:
		pass

