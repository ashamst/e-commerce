from django.db import models
from Admin.models import *
from seller.models import *

# Create your models here.
class cart_tb(models.Model):
    shippingaddress=models.CharField(max_length=20)
    contactnumber=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    totalprice=models.CharField(max_length=20)
    buyer_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,default=1)
    product_id=models.ForeignKey(product_tb,on_delete=models.CASCADE,default=1)

class order_tb(models.Model):
    shippingaddress=models.CharField(max_length=20)
    contactnumber=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    quantity=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
    totalprice=models.CharField(max_length=20)
    buyer_id=models.ForeignKey(register_tb,on_delete=models.CASCADE,default=1)
    product_id=models.ForeignKey(product_tb,on_delete=models.CASCADE,default=1)
    seller_id=models.ForeignKey(sellerregister_tb,on_delete=models.CASCADE,default=1)
