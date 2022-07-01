from django.shortcuts import render
from seller.models import *
from buyer.models import *
import datetime

# Create your views here.

def sellerHome(request):
    return render(request,'sellerHome.html')

def productUpload(request):
    category=category_tb.objects.all()
    return render(request,'productUpload.html',{'category':category})

def productuploadAction(request):
    pic=""
    if(len(request.FILES)>0):
        pic=request.FILES['file']
    else:
        pic="no pic"
    category=category_tb.objects.get(id=request.POST['category'])
    seller=sellerregister_tb.objects.get(id=request.session['seller_id'])
    file=product_tb(file=pic,name=request.POST['name'],details=request.POST['details'],stock=request.POST['stock'],price=request.POST['price'],category_id=category,seller_id=seller)
    file.save()
    category=category_tb.objects.all()
    return render(request,'productUpload.html',{'category':category,'msg':"Uploaded suuccessfully"})

def viewProduct(request):
    users=product_tb.objects.all()
    return render(request,'viewProduct.html',{'data':users})

def update(request,uid):
    user=product_tb.objects.filter(id=uid)
    return render(request,'update.html',{'data':user})

def updateAction(request):
    
    uid=request.POST['uid']
    product=product_tb.objects.get(id=uid)
    image=""
    if(len(request.FILES)>0):
        image=request.FILES['image']
    else:
        
        image=product.file
    name=request.POST['name']
    details=request.POST['details']
    stock=request.POST['stock']
    price=request.POST['price']
    product.name=name
    product.file=image
    product.details=details
    product.stock=stock
    product.price=price
    product.save()
    #user=product_tb.objects.filter(id=uid).update(file=image,name=name,details=details,stock=stock,price=price)
    user=product_tb.objects.filter(id=uid)
    return render(request,'update.html',{'data':user,'msg':"updated successfully"})

def delete(request,uid):
    user=product_tb.objects.filter(id=uid).delete()
    users=product_tb.objects.all()
    return render(request,'viewProduct.html',{'data':users})

def vieworder(request):
    users=order_tb.objects.filter(seller_id=request.session['seller_id'])
    return render(request,'vieworder.html',{'data':users})

def approve(request,uid):
    user=order_tb.objects.filter(id=uid).update(status='Approved')
    users=order_tb.objects.filter(seller_id=request.session['seller_id'])
    return render(request,'vieworder.html',{'data':users})

def reject(request,uid):
    user=order_tb.objects.filter(id=uid).update(status='Rejected')
    users=order_tb.objects.filter(seller_id=request.session['seller_id'])
    return render(request,'vieworder.html',{'data':users})

def verifycancel(request,uid):
    user=order_tb.objects.filter(id=uid).update(status='Cancel Verified')
    order=order_tb.objects.filter(id=uid)
    product=order[0].product_id
    quantity=int(order[0].quantity)
    newstock=int(product.stock)+quantity
    product.stock=newstock
    product.save()
    users=order_tb.objects.filter(seller_id=request.session['seller_id'])
    return render(request,'vieworder.html',{'data':users})

def trackingdetails(request,uid):
   return render(request,'trackingdetails.html',{'order_id':uid})

def trackingaction(request):
    trackingdetails=request.POST['trackingdetails']
    order_id=request.POST['order_id']
    order=order_tb.objects.get(id=order_id)
    user=tracking_tb(trackingdetails=trackingdetails,date=datetime.date.today(),time=datetime.datetime.now().strftime("%H:%M"),order_id=order)
    user.save()
    if ('delivered' in trackingdetails):
        user=order_tb.objects.filter(id=order_id).update(status='Delivered')
    return render(request,'trackingdetails.html',{'msg':"Tracking details updated",'order_id':order_id})
    
def supdate(request):
    user=sellerregister_tb.objects.filter(id=request.session['seller_id'])
    return render(request,'supdate.html',{'data':user})

def supdateaction(request):
    uid=request.session['seller_id']
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    dob=request.POST['dob']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    seller=sellerregister_tb.objects.filter(username=username).exclude(id=uid)
    buyer=register_tb.objects.filter(username=username)
    admin=Admin_tb.objects.filter(username=username)
    users=sellerregister_tb.objects.filter(id=uid)
    if seller.count()>0 or buyer.count()>0 or admin.count()>0:
        return render(request,'supdate.html',{'data':users,'msg':"Username already taken"})
    else:
        user=sellerregister_tb.objects.filter(id=uid).update(name=name,gender=gender,address=address,dob=dob,country=country,phone=phone,username=username)
        
        return render(request,'supdate.html',{'data':users,'msg':"Updated Successfully"})



