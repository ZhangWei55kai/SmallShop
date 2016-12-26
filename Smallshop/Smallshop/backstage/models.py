from __future__ import unicode_literals

from django.db import models
import uuid
from front.models import FrontUser
# Create your models here.
class Commodity(models.Model):
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	commodityName = models.CharField(max_length=30)
	commodityDes = models.TextField()
	commodityImg = models.URLField(max_length=100,blank=True)
	commodityStock = models.IntegerField()
	commodityPrice = models.DecimalField(max_digits=12,decimal_places=2)
	commodityCtime = models.DateField(auto_now_add=True)
	commondityCate = models.ForeignKey('CategoryModel')
	commondityTag = models.ManyToManyField('TagModel',blank=True)
	commodityPoints = models.IntegerField()
	
class CategoryModel(models.Model):
	name = models.CharField(max_length=20,unique=True)

class TagModel(models.Model):
	tagName = models.CharField(max_length=30,unique=True)


class ShoppingCart(models.Model):
	commodity = models.ForeignKey('Commodity')
	user = models.ForeignKey(FrontUser)
        cartCtime = models.DateField(auto_now_add=True)
    	buyNum = models.IntegerField(default=1)


class UserOrder(models.Model):
	orderSerial = models.UUIDField(default=uuid.uuid4,editable=False)
	user = models.ForeignKey(FrontUser)
	sendStatus = models.BooleanField(default=False)
	reveiceStatus = models.BooleanField(default=False)
	buyTime = models.DateTimeField(auto_now_add=True)
	commodity = models.ForeignKey('Commodity')
	orderPrice = models.DecimalField(max_digits=12,decimal_places=2)