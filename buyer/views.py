from django.shortcuts import render
from Admin.models import *
from seller.models import *
from buyer.models import *
import datetime

# Create your views here.

def home(request):
    return render(request,'home.html')

def viewProducts(request):
    users=product_tb.objects.all()
    return render(request,'viewProducts.html',{'data':users})

def viewMore(request,uid):
    users=product_tb.objects.filter(id=uid)
    return render(request,'viewMore.html',{'data':users})

def addtocart(request,uid):
    users=product_tb.objects.filter(id=uid)
    return render(request,'addtocart.html',{'data':users})

def cartAction(request):
    product_id=request.POST['product_id']
    buyer=register_tb.objects.get(id=request.session['buyer_id'])
    product_id=product_tb.objects.get(id=product_id)
    shippingaddress=request.POST['shippingaddress']
    contactnumber=request.POST['contactnumber']
    quantity=request.POST['quantity']
    totalprice=request.POST['totalprice']
    
    users=product_tb.objects.filter(id=request.POST['product_id'])
    if int(quantity)>int(product_id.stock):
        return render(request,'addtocart.html',{'msg':"Insufficient stock",'data':users})
    else:
        user=cart_tb(shippingaddress=shippingaddress,contactnumber=contactnumber,quantity=quantity,totalprice=totalprice,buyer_id=buyer,product_id=product_id)
        user.save()
        return render(request,'addtocart.html',{'msg':"Added to cart successfully",'data':users})

def viewCart(request):
    users=cart_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request,'viewCart.html',{'data':users})

def remove(request,uid):
    user=cart_tb.objects.filter(id=uid).delete()
    users=cart_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request,'viewCart.html',{'data':users})

def confirmorder(request):
    cartitems=request.POST.getlist('cartitem')
    for c in cartitems:
        cart=cart_tb.objects.filter(id=c)
        order=order_tb(shippingaddress=cart[0].shippingaddress,contactnumber=cart[0].contactnumber,quantity=cart[0].quantity,totalprice=cart[0].totalprice,buyer_id=cart[0].buyer_id,product_id=cart[0].product_id,seller_id=cart[0].product_id.seller_id,date=datetime.date.today(),status='pending')
        order.save()
        product=cart[0].product_id
        quantity=int(cart[0].quantity)
        newstock=int(product.stock)-quantity
        product.stock=newstock
        product.save()
        cart.delete()
    users=cart_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request,'viewCart.html',{'data':users,'msg':"Ordered successfully"})

def viewOrders(request):
    users=order_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request,'viewOrders.html',{'data':users})

def cancel(request,uid):
    user=order_tb.objects.filter(id=uid).update(status="canceled")
    users=order_tb.objects.filter(buyer_id=request.session['buyer_id'])
    return render(request,'viewOrders.html',{'data':users})
    
def viewtracking(request,uid):
    user=tracking_tb.objects.filter(order_id=uid)
    return render(request,'viewtracking.html',{'data':user})

def search(request):
    products=product_tb.objects.filter(name__contains=request.POST['search'])
    return render(request,'viewProducts.html',{'data':products})

def searchbyprice(request):
    category=category_tb.objects.all()
    return render(request,'searchbyprice.html',{'data':category})

def priceaction(request):
    products=product_tb.objects.filter(category_id=request.POST['category'],price__lte=request.POST['price'])
    return render(request,'viewProducts.html',{'data':products})

def bupdate(request):
    user=register_tb.objects.filter(id=request.session['buyer_id'])
    return render(request,'bupdate.html',{'data':user})

def bupdateaction(request):
    uid=request.session['buyer_id']
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    dob=request.POST['dob']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    seller=sellerregister_tb.objects.filter(username=username)
    buyer=register_tb.objects.filter(username=username).exclude(id=uid)
    admin=Admin_tb.objects.filter(username=username)
    users=register_tb.objects.filter(id=uid)
    if buyer.count()>0 or seller.count()>0 or admin.count()>0:
        return render(request,'bupdate.html',{'data':users,'msg':"Username already taken"})
    else:
        user=register_tb.objects.filter(id=uid).update(name=name,gender=gender,address=address,dob=dob,country=country,phone=phone,username=username)
        
        return render(request,'bupdate.html',{'data':users,'msg':"Updated Successfully"})


