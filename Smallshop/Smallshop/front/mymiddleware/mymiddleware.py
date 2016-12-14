# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-14 23:51:06
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-15 00:13:31
from front.models import FrontUser
from front import configs
def UserMiddleware(get_response):
	def middleware(request):
		sessionId = request.session.get(configs.LOGINED_KEY,None)
		if sessionId:
			user = FrontUser.objects.filter(pk=sessionId).first()
			if not hasattr(request,'userId'):
				setattr(request,'userId',user.pk)
			if not hasattr(request,'username'):
				setattr(request,'username',user.username)
			response = get_response(request)
			return response
		else:
			response = get_response(request)
			return response
	return middleware
