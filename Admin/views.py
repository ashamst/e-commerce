from django.shortcuts import render,redirect
from Admin.models import *
from buyer.models import *
from seller.models import *

# Create your views here.

def index(request):
    data=''
    if 'buyer_id' in request.session :
        data=product_tb.objects.all().order_by('-id')[:5]
    elif 'seller_id' in request.session:
        data=order_tb.objects.all().order_by('-id')[:5]
    elif 'admin_id' in request.session:
        data=sellerregister_tb.objects.all().order_by('-id')[:5]
        
    return render(request,'index.html',{'data':data})
    

def register(request):
    return render(request,'register.html')

def registerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    dob=request.POST['dob']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(username=username)
    seller=sellerregister_tb.objects.filter(username=username)
    admin=Admin_tb.objects.filter(username=username)
    if user.count()>0 or seller.count()>0 or admin.count()>0:
        return render(request,'register.html',{'msg':"Username already taken"})
    else:
        user=register_tb(name=name,gender=gender,address=address,dob=dob,country=country,phone=phone,username=username,password=password)
        user.save()
        return render(request,'register.html',{'msg':"Registration Succssess"})
    
def sellerRegisteration(request):
    return render(request,'sellerRegisteration.html')

def sellerregisterAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    dob=request.POST['dob']
    country=request.POST['country']
    phone=request.POST['phone']
    username=request.POST['username']
    password=request.POST['password']
    seller=sellerregister_tb.objects.filter(username=username)
    buyer=register_tb.objects.filter(username=username)
    admin=Admin_tb.objects.filter(username=username)
    if buyer.count()>0 or seller.count()>0 or admin.count()>0:
        return render(request,'sellerRegisteration.html',{'msg':"Username already taken"})
    else:
        user=sellerregister_tb(name=name,gender=gender,address=address,dob=dob,country=country,phone=phone,username=username,password=password,status='pending')
        user.save()
        return render(request,'sellerRegisteration.html',{'msg':"Registration Succssess"})

def login(request):
    return render(request,'login.html')

def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(username=username,password=password)
    seller=sellerregister_tb.objects.filter(username=username,password=password)
    admin=Admin_tb.objects.filter(username=username,password=password)
    if user.count()>0:
        request.session['buyer_id']=user[0].id
        return redirect('index')
    elif seller.count()>0:
        if seller[0].status == 'Approved':
            request.session['seller_id']=seller[0].id
            return redirect('index')
        else:
            return render(request,'login.html',{'msg':"You are not Approved"})
    elif admin.count()>0:
        request.session['admin_id']=admin[0].id
        return redirect('index')
    else:
        return render(request,'login.html',{'msg':"Incorrect username or password"})

def adminHome(request):
    return render(request,'adminHome.html')

def viewAllusers(request):
    users=sellerregister_tb.objects.all()
    return render(request,'viewAllusers.html',{'data':users})

def rejectUser(request,uid):
    user=sellerregister_tb.objects.filter(id=uid).update(status='rejected')
    users=sellerregister_tb.objects.all()
    return render(request,'viewAllusers.html',{'data':users})

def approveUser(request,uid):
    user=sellerregister_tb.objects.filter(id=uid).update(status='Approved')
    users=sellerregister_tb.objects.all()
    return render(request,'viewAllusers.html',{'data':users})

def addCategory(request):
    return render(request,'addCategory.html')

def addCategoryaction(request):
     name=request.POST['name']
     user=category_tb(name=name)
     user.save()
     return render(request,'addCategory.html',{'msg':"Added suuccessfully"})

def logout(request):
    if 'buyer_id' in request.session:
        del request.session['buyer_id']
    if 'seller_id' in request.session:
        del request.session['seller_id']
    if 'admin_id' in request.session:
        del request.session['admin_id']
        
    return render (request,'index.html')

def forgot(request):
    return render(request,'forgot.html')


def forgotaction(request):
    username=request.GET['usernam']
    buyer=register_tb.objects.filter(username=username)
    seller=sellerregister_tb.objects.filter(username=username)
    

    if buyer.count()>0 or seller.count()>0:
        return render(request,'password.html',{'data':username})
    else:
        return render(request,'forgot.html',{'msg':"username doesnot exist"})

def passwordaction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    phone=request.POST['phone']
    username=request.POST['username']
    buyer=register_tb.objects.filter(name=name,dob=dob,phone=phone,username=username)
    seller=sellerregister_tb.objects.filter(name=name,dob=dob,phone=phone,username=username)
    if buyer.count()>0 or seller.count()>0:
        return render(request,'newpass.html',{'data':username})
    else:
        return render(request,'password.html',{'msg':"user doesnt exist"})

def passaction(request):
    newpassword=request.POST['newpassword']
    username=request.POST['username']
    buyer=register_tb.objects.filter(username=username)
    seller=sellerregister_tb.objects.filter(username=username)
    if buyer.count()>0:
       buyer.update(password=newpassword)
    else:
        seller.update(password=newpassword)
    return render(request,'login.html',{'msg':"Updated successfully"})
    
        
