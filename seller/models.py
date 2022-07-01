from django.db import models
from Admin.models import *
from buyer.models import *
from seller.models import *

# Create your models here.

class product_tb(models.Model):
    seller_id=models.ForeignKey(sellerregister_tb,on_delete=models.CASCADE,default=1)
    file=models.FileField()
    name=models.CharField(max_length=20)
    details=models.CharField(max_length=20)
    stock=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    category_id=models.ForeignKey(category_tb,on_delete=models.CASCADE,default=1)

class tracking_tb(models.Model):
    trackingdetails=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    order_id=models.ForeignKey('buyer.order_tb',on_delete=models.CASCADE,default=1)
    
