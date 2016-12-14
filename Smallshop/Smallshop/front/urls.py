# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-12 22:19:30
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-14 20:49:53
from django.conf.urls import url,include
from django.contrib import admin
from views import front_login,front_register,front_logout,shopCart,addShop,front_index

urlpatterns = [
    url(r'^login/',front_login,name='front_login'),
    url(r'^register/',front_register,name='front_register'),
    url(r'^logout/',front_logout,name='front_logout'),
    url(r'^shopCart/',shopCart,name='shop_cart'),
    url(r'^addShop/?P<commodityId>',addShop,name='add_shop'),
    url(r'^index/',front_index,name='front_index'),
]
