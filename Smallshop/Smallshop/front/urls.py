# -*- coding: utf-8 -*-
# @Author: zhangwei
# @Date:   2016-12-12 22:19:30
# @Last Modified by:   zhangwei
# @Last Modified time: 2016-12-17 04:00:24
from django.conf.urls import url,include
from django.contrib import admin
from views import front_login,front_register,front_logout,shopCart,addShopCart,front_index,addOrder

urlpatterns = [
    url(r'^login/',front_login,name='front_login'),
    url(r'^register/',front_register,name='front_register'),
    url(r'^logout/',front_logout,name='front_logout'),
    url(r'^shopCart/',shopCart,name='shop_cart'),
    url(r'^addShop/(?P<commodityId>\w+)',addShopCart,name='add_shopCart'),
    url(r'^index/',front_index,name='front_index'),
    url(r'^addOrder/',addOrder,name='add_Order')
]
