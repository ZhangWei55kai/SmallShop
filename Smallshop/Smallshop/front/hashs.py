# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-11 22:44:24
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-11 22:57:21
import hashlib
import configs

def make_password(raw_passwrd,salt=None):
	if not salt:
		salt = configs.PASSWORD_SALT
	hash_password = hashlib.md5(configs.PASSWORD_SALT+raw_password).hexdigest()
	return hash_password

def check_password(raw_password,hash_password):
	if not raw_password:
		return False
	tmpPassword = make_password(raw_password)
	if tmpPassword == hash_password:
		return True
	else:
		return False