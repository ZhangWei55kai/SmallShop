#coding:utf-8
from __future__ import unicode_literals

from django.db import models
import hashs
import configs
# Create your models here.
class FrontUser(models.Model):

	name = models.CharField(max_length=30)
	email = models.EmailField()
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	points = models.IntegerField(default=0)
	vipLevel = models.IntegerField(default=0)
	createtime = models.DateField(auto_now_add=True)
	balance = models.DecimalField(default=0,decimal_places=2,max_digits=12,)
	
	#首次save的时候保存加密并传入init方法
	def __init__(self,*args,**kwargs):
		if 'password' in kwargs:
			password = kwargs['password']
			hash_password = hashs.make_password(password)
			kwargs['password'] = hash_password
		super(FrontUser,self).__init__(*args,**kwargs)

	#检测输入的密码是不是和数据库中的密码一样	
	def check_password(self,raw_password):
		return hashs.check_password(raw_password,self.password)

	#重新设置密码
	def set_password(self,raw_password):
		if not raw_password:
			return False
		hash_password = hashs.make_password(raw_password)
		self.password = hash_password
		self.save(update_fields=['password'])