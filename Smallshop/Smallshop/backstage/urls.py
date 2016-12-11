# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-10 19:25:35
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-11 13:50:04
from django.conf.urls import url,include
from django.contrib import admin
from views import createCommodity,addCategory,addTag

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/',createCommodity,name='create_commodity'),
    url(r'^addCategory/',addCategory,name='add_Category'),
    url(r'^addTag/',addTag,name='add_Tag'),
]
