# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-10 19:25:35
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-10 20:44:14
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import request,JsonResponse
from forms import MyLogin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from models import Commodity
from forms import CommodityForm
# Create your views here.

def index_login(request):
	if request.method=='GET':
		return render(request,'index.html')
	else:
		form = MyLogin(request.POST)
		if form.is_valid():	#检验是否合法
			# print dir(form)
			# 检查数据是否存在
			# 1. 获取数据进行对比
			username=form.cleaned_data.get('username',None)
			password=form.cleaned_data.get('password',None)
			user = authenticate(username=username,password=password)
			if user:
				login(request,user)
				return HttpResponseRedirect(reverse('login'))
			else:
				return HttpResponse(u'登录失败!')
		else:
			return HttpResponse(u'表单验证失败')

# 注册User
def index_register(request):
	User.objects.create_user(username='django',password='123456')
	return HttpResponse(u'OK')

def set_pwd(request):
	user = User.objects.filter(username='django').first()
	user.set_password('666666')
	user.save()
	return HttpResponse(u'update pwd OK')

def index_logout(request):
	if request.method=='POST':
		logout(request)
	return render(request,'end.html',{'user':request.user})



def errorMess(error):
	errorm = ''
	for k,v in error.items():
		errorm = v
	return errorm

	
@login_required
def createCommodity(request):
	if request.method == 'GET':
		return render(request,'html')
	else:
		commodity = CommodityForm(request.POST)
		commodityName = request.POST.get('commodityName',None)
		if commodity.is_valid():
			commodityName = commodity.cleaned_data.get('commodityName',None) 
			commodityDes = commodity.cleaned_data.get('commodityDes',None) 
			commodityImg = commodity.cleaned_data.get('commodityImg',None) 
			commodityStock = commodity.cleaned_data.get('commodityStock',None) 
			commodityPrice = commodity.cleaned_data.get('commodityPrice',None) 
			commodityModel = Commodity(commodityName=commodityName,
				commodityDes=commodityDes,
				commodityImg=commodityImg,
				commodityStock=commodityStock,
				commodityPrice=commodityPrice,
				)
			commodityModel.save()
			return JsonResponse({'message':u'创建成功'})
		else:
			return JsonResponse({'error':errorMess(commodity.errors)})
