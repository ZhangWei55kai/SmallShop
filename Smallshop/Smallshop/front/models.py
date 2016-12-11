from __future__ import unicode_literals

from django.db import models
import hashs
# Create your models here.
class FrontUser(models.Model):


	#首次save的时候保存加密并传入init方法
	def __init__(self,*args,**kwargs):
		if 'password' in kwargs:
			password = kwargs['password']
			password = hashs.make_password(password)
			kwargs['password'] = password
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