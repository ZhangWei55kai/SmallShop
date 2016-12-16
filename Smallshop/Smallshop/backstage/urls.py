# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-10 19:25:35
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-17 02:21:09
from django.conf.urls import url,include
from django.contrib import admin
from views import createCommodity,addCategory,addTag
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/',createCommodity,name='create_commodity'),
    url(r'^addCategory/',addCategory,name='add_Category'),
    url(r'^addTag/',addTag,name='add_Tag'),
    url(r'^test/',views.test)
]
