# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-11 23:55:29
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-12 00:09:00
import configs
from django.shortcuts import redirect,reverse
from models import FrontUser
def front_login_required(func):
	def wrapper(request,*args,**kwargs):
		#获取session中的uid
		uid = request.session[configs.LOGINED_KEY]
		#如果获取到了表示用户已经登陆了，并且执行传过来的方法
		if uid:
			# result = FrontUser.objects.filter(pk=uid).first()
			# if result:
			func(request,*args,**kwargs)
		else:
			#获取当前访问的url
			url = request.path
			#login之后通过request.GET.get('next')写判断，如果有就跳转next中的url
			#否则就跳转login的url
			return redirect(reverse('front_login') + '?next='+url)
	return wrapper