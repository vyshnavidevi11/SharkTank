from django.shortcuts import render,redirect
from django.contrib import messages
from mainapp.models import User
from userapp.models import Predict
# Create your views here.

def home(req):
    return render(req,'main_template/index.html')

def prediction_results(req,id):
    pred = Predict.objects.get(predict_id=id)
    return render(req,'main_template/prediction-result.html',{'p':pred})

def contact(req):
    return render(req,'main_template/contact.html')

def user_register(req):
    if req.method == "POST" and req.FILES['image']:
        fullname=req.POST.get("fullname")
        email=req.POST.get("email")
        phone=req.POST.get("phonenumber")
        pwd=req.POST.get("password")
        city=req.POST.get("city")
        industry=req.POST.get("industry")
        img=req.FILES['image']
        state=req.POST.get("state")
        print(fullname,email,phone,pwd,city,industry,img,state)
        User.objects.create(Fullname=fullname,Email=email,Phone=phone,Password=pwd,city=city,industry=industry,image=img,state=state)
        messages.success(req,'User has registered')
        return redirect('user_register')
    return render(req,'main_template/user-register.html')

