# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-10 19:25:35
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-26 22:48:38
from django.conf.urls import url,include
from django.contrib import admin
from views import createCommodity,addCategory,addTag
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create/',createCommodity,name='create_commodity'),
    url(r'^addCategory/',addCategory,name='add_Category'),
    url(r'^addTag/',addTag,name='add_Tag'),
    url(r'^test/',views.test),
    url(r'login/',views.index_login,name='index_login'),
    url(r'^index/',views.back_index,name='index'),
    url(r'^logout/',views.index_logout,name='index_logout'),
    url(r'^createCommodity/',views.createCommodity,name='b_createCommodity'),
    url(r'^editCommodity/(?P<commodityId>[^/]+)',views.editCommodity,name='b_editCommodity')
]
