from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Commodity(models.Model):
	commodityName = models.CharField(max_length=30)
	commodityDes = models.TextField()
	commodityImg = models.URLField(max_length=100,blank=True)
	commodityStock = models.IntegerField()
	commodityPrice = models.IntegerField()
	commodityCtime = models.DateField(auto_now_add=True)

