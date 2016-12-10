# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-10 19:25:35
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-10 19:29:25
from django.conf.urls import url,include
from django.contrib import admin
from views import createCommodity

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/',createCommodity,name='create_commodity')
]
