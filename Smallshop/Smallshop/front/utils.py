# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-11 23:35:52
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-11 23:46:03
import configs
def login(request,username,password):
	user = FrontUser.objects.filter(username=username).first()
	if user:
		result = user.check_password(password)
		if result:
			request.session[configs.LOGINED_KEY] = str(user.uid)
			return user
		else:
			return False
	else:
		return False

def logout(request):
	try:
		del request.session[configs.LOGINED_KEY]
	except ValueError:
		pass