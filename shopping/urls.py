"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Admin import views as admin_view
from buyer import views as buyer_view
from seller import views as seller_view
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',admin_view.index,name='index'),
    url(r'^register/',admin_view.register,name='register'),
    url(r'^registerAction/',admin_view.registerAction,name='registerAction'),
    url(r'^sellerRegisteration/',admin_view.sellerRegisteration,name='sellerRegisteration'),
    url(r'^sellerregisterAction/',admin_view.sellerregisterAction,name='sellerregisterAction'),
    url(r'^login/',admin_view.login,name='login'),
    url(r'^loginAction/',admin_view.loginAction,name='loginAction'),
    url(r'^home/',buyer_view.home,name='home'),
    url(r'^sellerHome/',seller_view.sellerHome,name='sellerHome'),
    url(r'^adminHome/',admin_view.adminHome,name='adminHome'),
    url(r'^viewAllusers/',admin_view.viewAllusers,name='viewAllusers'),
    url(r'^rejectUser/(?P<uid>\d+)/$',admin_view.rejectUser,name='rejectUser'),
    url(r'^approveUser/(?P<uid>\d+)/$',admin_view.approveUser,name='approveUser'),
    url(r'^productUpload/',seller_view.productUpload,name='productUpload'),
    url(r'^productuploadAction/',seller_view.productuploadAction,name='productuploadAction'),
    url(r'^addCategory/',admin_view.addCategory,name='addCategory'),
    url(r'^addCategoryaction/',admin_view.addCategoryaction,name='addCategoryaction'),
    url(r'^viewProduct/',seller_view.viewProduct,name='viewProduct'),
    url(r'^update/(?P<uid>\d+)/$',seller_view.update,name='update'),
    url(r'^updateAction/',seller_view.updateAction,name='updateAction'),
    url(r'^delete/(?P<uid>\d+)/$',seller_view.delete,name='delete'),
    url(r'^viewProducts/',buyer_view.viewProducts,name='viewProducts'),
    url(r'^viewMore/(?P<uid>\d+)/$',buyer_view.viewMore,name='viewMore'),
    url(r'^addtocart/(?P<uid>\d+)/$',buyer_view.addtocart,name='addtocart'),
    url(r'^cartAction/',buyer_view.cartAction,name='cartAction'),
    url(r'^viewCart/',buyer_view.viewCart,name='viewCart'),
    url(r'^remove/(?P<uid>\d+)/$',buyer_view.remove,name='remove'),
    url(r'^confirmorder/',buyer_view.confirmorder,name='confirmorder'),
    url(r'^viewOrders/',buyer_view.viewOrders,name='viewOrders'),
    url(r'^vieworder/',seller_view.vieworder,name='vieworder'),
    url(r'^cancel/(?P<uid>\d+)/$',buyer_view.cancel,name='cancel'),
    url(r'^approve/(?P<uid>\d+)/$',seller_view.approve,name='approve'),
    url(r'^reject/(?P<uid>\d+)/$',seller_view.reject,name='reject'),
    url(r'^verifycancel/(?P<uid>\d+)/$',seller_view.verifycancel,name='verifycancel'),
    url(r'^trackingdetails/(?P<uid>\d+)/$',seller_view.trackingdetails,name='trackingdetails'),
    url(r'^trackingaction/',seller_view.trackingaction,name='trackingaction'),
    url(r'^viewtracking/(?P<uid>\d+)/$',buyer_view.viewtracking,name='viewtracking'),
    url(r'^search/',buyer_view.search,name="search"),
    url(r'^searchbyprice/',buyer_view.searchbyprice,name='searchbyprice'),
    url(r'^priceaction/',buyer_view.priceaction,name='priceaction'),
    url(r'^bupdate/',buyer_view.bupdate,name='bupdate'),
    url(r'^bupdateAction/',buyer_view.bupdateaction,name='bupdateaction'),
    url(r'^supdate/',seller_view.supdate,name='supdate'),
    url(r'^supdateaction/',seller_view.supdateaction,name='supdateaction'),
    
    url(r'^logout/',admin_view.logout,name='logout'),
    url(r'^forgot/',admin_view.forgot,name='forgot'),
    url(r'^forgotaction/',admin_view.forgotaction,name='forgotaction'),
    url(r'^passwordaction/',admin_view.passwordaction,name='passwordaction'),
    url(r'^passaction/',admin_view.passaction,name='passaction'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
