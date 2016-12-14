# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-12 21:22:50
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-14 22:45:31
from django import forms
from models import FrontUser
class Frontuser_login(forms.Form):
	username = forms.CharField(min_length=6)
	password = forms.CharField(min_length=6)
	remember = forms.BooleanField(required=False)

class Frontuser_reg(forms.Form):
	name = forms.CharField(max_length=30)
	email = forms.EmailField()
	username = forms.CharField(min_length=6)
	password = forms.CharField(min_length=6)
	repassword = forms.CharField(min_length=6)
	address = forms.CharField(min_length=3)

	def clean_username(self):
		username = self.cleaned_data.get('username',None)
		oldUsername = FrontUser.objects.filter(username__contains=username).first()
		if oldUsername:
			raise forms.ValidationError(u'用户名不能重复',code = 'repeatError')
		return username

	def clean_password(self):
		password = self.cleaned_data.get('password',None)
		repassword = self.cleaned_data.get('repassword',None)
		if password and repassword and password != repassword:
			raise forms.ValidationError(u'两次输入的用户名不一致',code='inputError')
		return password