from __future__ import unicode_literals

from django.db import models
import uuid
# Create your models here.
class Commodity(models.Model):
	uid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	commodityName = models.CharField(max_length=30)
	commodityDes = models.TextField()
	commodityImg = models.URLField(max_length=100,blank=True)
	commodityStock = models.IntegerField()
	commodityPrice = models.IntegerField()
	commodityCtime = models.DateField(auto_now_add=True)
	commondityCate = models.ForeignKey('CategoryModel')
	commondityTag = models.ManyToManyField('TagModel',null=True)

class CategoryModel(models.Model):
	name = models.CharField(max_length=20,unique=True)

class TagModel(models.Model):
	tagName = models.CharField(max_length=30,unique=True)
