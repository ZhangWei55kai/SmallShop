# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-10 19:25:35
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-11 15:25:07
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.http import request,JsonResponse
from forms import MyLogin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from models import Commodity,CategoryModel,TagModel
from forms import CommodityForm,CategoryForm,TagForm
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

	
# @login_required
def createCommodity(request):
	if request.method == 'GET':
		return render(request,'html')
	else:
		commodity = CommodityForm(request.POST)
		if commodity.is_valid():
			commodityName = commodity.cleaned_data.get('commodityName',None) 
			commodityDes = commodity.cleaned_data.get('commodityDes',None) 
			commodityImg = commodity.cleaned_data.get('commodityImg',None) 
			commodityStock = commodity.cleaned_data.get('commodityStock',None) 
			commodityPrice = commodity.cleaned_data.get('commodityPrice',None) 
			categoryId = commodity.cleaned_data.get('categoryId',None)
			tag = request.POST.getlist('tags',None)
			print tag
			category = CategoryModel.objects.filter(pk=categoryId).first()
			commodityModel = Commodity(commodityName=commodityName,
				commodityDes=commodityDes,
				commodityImg=commodityImg,
				commodityStock=commodityStock,
				commodityPrice=commodityPrice,
				commondityCate=category
				)
			commodityModel.save()
			tagModel = TagModel.objects.filter(pk__in=tag)
			commodityModel.commondityTag.set(tagModel)
			return JsonResponse({'message':u'创建成功'})
		else:
			return JsonResponse({'error':errorMess(commodity.errors)})


# @login_required
def addCategory(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			categoryName = form.cleaned_data.get('categoryName',None)
			oldcategory = CategoryModel.objects.filter(name=categoryName).first()
			if not oldcategory:
				categoryModel = CategoryModel(name=categoryName)
				categoryModel.save()
				return JsonResponse({'code':200})
			else:
				return JsonResponse({'error':u'不能创建同名的分类'})
		else:
			return JsonResponse({'error':errorMess(form.errors)})


# @login_required
def addTag(request):
	if request.method == 'POST':
		form = TagForm(request.POST)
		if form.is_valid():
			tagName = form.cleaned_data.get('tagName',None)
			oldtag = TagModel.objects.filter(tagName=tagName).first()
			if not oldtag:
				tagModel = TagModel(tagName=tagName)
				tagModel.save()
				return JsonResponse({'code':200})
			else:
				return JsonResponse({'error':u'不能创建同名的标签'})
		else:
			return JsonResponse({'error':errorMess(form.errors)})



