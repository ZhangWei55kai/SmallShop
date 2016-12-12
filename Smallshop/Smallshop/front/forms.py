# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-12 21:22:50
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-12 23:59:03
from django import forms

class Frontuser_login(forms.Form):
	username = forms.CharField(min_length=6)
	password = forms.CharField(min_length=6)

class Frontuser_reg(forms.Form):
	name = forms.CharField(max_length=30)
	email = forms.EmailField()
	username = forms.CharField(min_length=6)
	password = forms.CharField(min_length=6)
	address = forms.CharField(min_length=3)

	def clean_username(self):
		username = self.cleaned_data.get('username',None)
		oldUsername = Commodity.objects.filter(username__contains=username).first()
		if oldUsername:
			raise forms.ValidationError(u'用户名不能重复',code = 'repeatError')
		return oldUsername