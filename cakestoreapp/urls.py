from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    #path('cakes',views.cakes,name='cakes'),
    path('addtocart/<int:id>',views.addtocart,name='addtocart'),
    path('feed',views.feedback,name='feed'),
    path('about',views.about,name='about'),
    path('register',views.addcustomer,name='register'),
    path('log',views.log,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('display',views.displaycake,name='display'),
    path('display<str:slug>',views.displayview,name='displayview'),
    #path('display/<str:category_name_slug>/<str:cakename_slug>',views.displayview,name='displayview'),
    path('dispfeedbacks',views.dispfeedback,name='dispfeedbacks'),
    path('logout',views.logout,name='logout'),
    path('disp',views.carts,name='disp'),
    path('place',views.placeorder,name='place'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('order',views.order,name='order'),
    path('checkoutform',views.ordercheckout,name='checkoutform'),
    path('confirm/<int:id>',views.confirm,name='confirm'),
    path('orders2',views.order2,name='orders2'),
    path('gallery',views.gallery,name='gallery'),
    path('remove/<int:id>',views.remove,name='remove'),
    

    
    

    
   
]