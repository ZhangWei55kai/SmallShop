# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-10 18:57:34
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-22 21:34:51
from django import forms
from models import Commodity
class MyLogin(forms.Form):
	username=forms.CharField(required=True,min_length=3)
	password=forms.CharField(required=True,min_length=3)

class CommodityForm(forms.Form):
	commodityName = forms.CharField(max_length=30)
	commodityDes = forms.CharField()
	commodityImg = forms.URLField()
	commodityStock = forms.IntegerField()
	commodityPrice = forms.DecimalField()
	categoryId = forms.IntegerField(required=True)
	points = forms.IntegerField(required=True)

	def clean_commodityName(self):
		commodityName = self.cleaned_data.get('commodityName',None)
		oldCommodity = Commodity.objects.filter(commodityName__contains=commodityName).first()
		if oldCommodity:
			raise forms.ValidationError(u'商品名称不能重复',code = 'repeatError')
		return commodityName

	def clean_commodityImg(self):
		commodityImg = self.cleaned_data.get('commodityImg',None)
		if not commodityImg:
			raise forms.ValidationError(u'请上传图片',code = 'min_length')
		return commodityImg

	def clean_commodityStock(self):
		commodityStock = self.cleaned_data.get('commodityStock',None)
		if not commodityStock:
			raise forms.ValidationError(u'库存不能为空',code = 'min_length')
		return commodityStock

	def clean_commodityPrice(self):
		commodityPrice = self.cleaned_data.get('commodityPrice',None)
		if not commodityPrice:
			raise forms.ValidationError(u'价格不能为空',code = 'min_length')
		return commodityPrice

class CategoryForm(forms.Form):
	categoryName = forms.CharField(max_length=20)

class TagForm(forms.Form):
	tagName = forms.CharField(max_length=30)

class OrderForm(forms.Form):
	pass