#coding:utf-8
from django.shortcuts import render,redirect,reverse
from django.http import request,JsonResponse,HttpResponse
from forms import Frontuser_login,Frontuser_reg
from utils import login,logout
from decorators import front_login_required
from hashs import make_password
from models import FrontUser
from backstage.models import UserOrder
from backstage.models import Commodity,ShoppingCart
from django.db.models import Q
import configs
# Create your views here.
def front_register(request):
	if request.method == 'GET':
		return render(request,'sign.html')
	else:
		frontReg_form = Frontuser_reg(request.POST)
		if frontReg_form.is_valid():
			name = frontReg_form.cleaned_data.get('name',None)
			email = frontReg_form.cleaned_data.get('email',None)
			username = frontReg_form.cleaned_data.get('username',None)
			password = frontReg_form.cleaned_data.get('password',None)
			address = frontReg_form.cleaned_data.get('address',None)
			frontUser = FrontUser(name=name,
								  email=email,
								  username=username,
								  password=password,
								  address=address)
			frontUser.save()
			login(request,username,password)
			return JsonResponse({'code':200})
		else:
			return JsonResponse({'error':frontReg_form.errors})

def front_login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		frontUser_form = Frontuser_login(request.POST)
		if frontUser_form.is_valid():
			username = frontUser_form.cleaned_data.get('username',None)
			password = frontUser_form.cleaned_data.get('password',None)
			remember = frontUser_form.cleaned_data.get('remember',None)
			if login(request,username,password):
				if remember:
					request.session.set_expiry(600)
				else:
					request.session.set_expiry(0)
				return JsonResponse({'message':u'登陆成功'})
			else:
				return JsonResponse({'error':u'用户名或密码错误'})
		else:
			return JsonResponse({'error':'用户名或密码格式不正确'})


@front_login_required
def front_logout(request):
	logout(request)
	return redirect('login.html')

@front_login_required
def shopCart(request):
	if request.method == 'GET':
		userId = request.session[configs.LOGINED_KEY]
		shopcart = ShoppingCart.objects.filter(user=userId).all()
		shopcartList = shopcart.commodity
		commodity = Commodity.objects.filter(uid__in=shopcartList)
		context = {'commodity':commodity}
		return JsonResponse('1111')

# @front_login_required
def addShopCart(request,commodityId):
#把商品的ID放在a标签中直接放入购物车
	if request.method == 'GET':
		userId = request.userId
		shoppingcart = ShoppingCart(commodity_id=commodityId,user_id=userId)
		shoppingcart.save()
		return redirect(reverse('shop_cart'))


# @front_login_required
#get订单详情界面
#使用ajax将购物车勾选的id传入到该函数中，用request的方法去找
def addOrder(request):
	if request.method == 'GET':
		userId = request.userId
		cartId = request.POST.getlist('CartIds',None)
		shoppingcart = ShoppingCart.objects.filter(Q(user=userId)&Q(pk__in=cartId)).all()
		user = request.username
		#通过外键访问用户名等等信息
		commodity = shoppingcart.commodity
		context = {'cart':shoppingcart,
				   'user':user,
				   'commidityName':commodityName,
				   'uid':uid,
				   'buyNum':shoppingcart}
		return render(request,'order.html',context)
	else:
		#将购买的商品和购买的数量逐个拆出来进行计算，一个商品存为一个订单，商品id尽量在后期通过ajax方法传入函数中
		#本次方法经测试，是可以实现购买生成订单功能
		user = request.userId
		cartId = request.POST.getlist('CartIds',None)
		shoppingcart = ShoppingCart.objects.filter(commodity_id__in=cartId).all()
		print shoppingcart
		commodityAll = []
		for i in shoppingcart:
			type(i.commodity)
			commodityAll.append(i.commodity)
		allCommodityId = []
		for cId in commodityAll:
			allCommodityId.append(cId.uid)
		allCommodityPrice = []
		for price in commodityAll:
			allCommodityPrice.append(price.commodityPrice)
		allCommodityNum = []
		for num in shoppingcart:
			allCommodityNum.append(num.buyNum)
		priceAccount = [i[0]*i[1] for i in zip(allCommodityPrice,allCommodityNum)]
		for order in range(len(priceAccount)):
			userOrder = UserOrder(user_id=user,commodity_id=allCommodityId[order],orderPrice=priceAccount[order])
			userOrder.save()
		return JsonResponse({'code':'200'})
		


#首页
@front_login_required
def front_index(request):
	if request.method == 'GET':
		print request.username
		return render(request,'index.html')



