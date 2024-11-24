from django.shortcuts import render,redirect
from.models import Customer,Cakes,Feedbacks,Cart,Orders,Category
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse
import razorpay

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    response={}
    try:
        un=request.POST['username']
        fdback=request.POST['fb']
        feedbacklist=Feedbacks(username=un,feedback=fdback)
        feedbacklist.save()
        response['msg']='Feedback Added Successfully'
        return render(request,'feedback.html',response)
    except Exception as e:
        print(e)
        response['msg']='Not Added'
    return render(request, 'feedback.html',response)

def dispfeedback(request):
    fbdtls=Feedbacks.objects.all()
    return render(request, 'feedback2.html',{'fd':fbdtls})

def addcustomer(request):
    response={}
    try:
        if request.method=='POST':
            fn=request.POST['firstname']
            ln=request.POST['lastname']
            username=request.POST['username']
            em=request.POST['email']
            num=int(request.POST['mobile'])
            loc=request.POST['location']
            password=request.POST['password']
            cpwd=request.POST['cpassword']
            #if User.objects.filter(username=username).exists():
                #response['msg']='Username Already Exists'
            if password==cpwd:
                if User.objects.filter(username=username).exists():
                    response['msg']='Username Already Exists'
                else:
                    customerlist=Customer(first_name=fn,last_name=ln,username=username,mobile_number=num,email=em,location=loc,password=password,confirmpassword=cpwd)
                    customerlist.save()
                    reguser=User.objects.create_user(username=username,password=password)
                    reguser.save()
                response['msg']='Registered Successfully'
            else:
                response['msg']='Your Password and Confirm Password did not Match'
        return render(request, 'regform.html',response)
    except Exception as e:
        print(e)
        response['msg']='not registered'
        return render(request, 'regform.html',response)

def log(request):
    #response={}
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('adminhome')
            if user.is_active:
                return redirect('userhome')
        else:
            messages.info(request, "invalid login")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def userhome(request):
    return render(request, 'userhome.html')

def displaycake(request):
    '''ct=Category.objects.all()
    cakedtls=Cakes.objects.all()
    p={'ck':cakedtls,'chk':ct}
    return render(request,'cakes.html',{'ck':cakedtls,'ctg':ct})'''
    ct=Category.objects.filter(status=0)
    cakedtls=Cakes.objects.all()
    return render(request,'cakes.html',{'ck':cakedtls,'ctg':ct})
    
def displayview(request,slug):
    if Category.objects.filter(slug=slug,status=0):
        cake=Cakes.objects.filter(category_name__slug=slug)
        return render(request,'cakes2.html',{'cake':cake})
    else:
        messages.error(request,"no such category")
        return redirect('display')
      
def addtocart(request,id):
    cakedtls=Cakes.objects.get(id=id)
    itemlist=Cart(cakename=cakedtls.cakename,price=cakedtls.price,cakeimage=cakedtls.cakeimage)
    itemlist.save()
    return redirect('userhome')
    
    
def carts(request):
    cart=Cart.objects.all()
    total_items=Cart.objects.count()
    totals= Cart.objects.annotate(totals=Sum('price'))
    total=0
    for i in cart:
        total=total+i.price
    total_amt=total
    return render(request,'mycart.html',{'c':cart,'t':total_items,'ta':total_amt})
    
def placeorder(request):
    return render(request,'placeorder.html')

def adminhome(request):
    return render(request,'adminhome.html')

def order(request):
    od=Orders.objects.all()
    return render(request,'orders.html',{'order':od})
def ordercheckout(request):
    un=request.POST['uname']
    em=request.POST['email']
    ad=request.POST['address']
    loct=request.POST['loc']
    zipcode=int(request.POST['zip'])
    ed=request.POST['dt']
    #et=request.POST['tm']
    cart=Cart.objects.all()
    totals= Cart.objects.annotate(totals=Sum('price'))
    total=0
    for i in cart:
        total=total+i.price
    total_amt=total
    if request.POST['paymentmethod']=='Cash On Delivery':
        od=Orders(customer=un,amount=total_amt,address=ad,status='pending')
        od.save()
        cart=Cart.objects.all()
        cart.delete()
        order_dtls=Orders.objects.all()
        return render(request,'success.html',{'odrs':order_dtls,'name':un,'address':ad,'location':loct,'amt':total_amt})
    else:
        totals= Cart.objects.annotate(totals=Sum('price'))
        total=0
        for i in cart:
            total=total+i.price
        total_amt=total
        amt=total_amt*100
        od=Orders(customer=un,amount=total_amt,address=ad,status='pending')
        od.save()
        cart=Cart.objects.all()
        cart.delete()
        order_dtls=Orders.objects.all()
        client = razorpay.Client(auth=("rzp_test_BxZvEpl01zwGtx","YI8wYJqkAXi7vGiTUcOSaOgN"))
        payment = client.order.create({'amount': amt, 'currency': 'INR','payment_capture': '1'})
        print(payment)
        return render(request,'onlinepayment.html',{'payment':payment,'name':un,'amt':total_amt})

def onlinesuccess(request):
    return render(request,'onlinesuccess.html')

def confirm(request,id):
    Orders.objects.filter(id=id).update(status="Delivered")
    return redirect('order')

def remove(request,id):
    dc=Cart.objects.filter(id=id)
    dc.delete()
    return redirect('disp')

def order2(request):
    return render(request,'orders2.html')

def gallery(request):
    return render(request,'gallery.html')
    #fbdtls=Feedbacks.objects.all()
    #return render(request, 'feedback2.html',{'fd':fbdtls})














    



