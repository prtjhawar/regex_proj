from django.shortcuts import render,HttpResponse,redirect

from .models import my_cv
from .forms import cv_form ,register_from
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate  ,login ,logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def forms(request):
    if request.method=="POST":
            a =  cv_form(request.POST,request.FILES)
            if a.is_valid():

                a.save()
        
              
                return redirect('/index/')

            
            


            
        
    
    a = cv_form()
    context = {

        'a':a
    }
    return render(request,'forms.html',context)

def get(request):
    
    data=my_cv.objects.filter(user=request.user)
    print(data)

    context={
        'data':data

    }
    return render(request,'index.html',context)

def create_account(request):
    if request.method == "POST":
        x = register_from(request.POST)
        if x.is_valid():
            x.save()
            return HttpResponse('data saved!!')
        
    x = register_from()
    my_dict = {
        'x' : x
    }
    return render(request,'auth_forms.html',my_dict)

def login_form(request):
    if request.method == "POST":
        x = AuthenticationForm(data = request.POST)
        print('>>>>x',x)
        if x.is_valid():
            uname = x.cleaned_data['username']
            passw = x.cleaned_data['password']
            user = authenticate(username = uname,password = passw)
            if user is not None:
                login(request,user)
                return redirect('/forms/')
            
    x =AuthenticationForm()
    context = {
                'x':x
        }
    return render(request,'login_form.html',context)
        
def get_out(request):
    logout(request)
    return redirect('/login/')

def Create_Account(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        print(uname,email,passw)
        
        if User.objects.filter(username=uname).first():
            messages.success(request,'username is taken')

        if User.objects.filter(email=email).first():
            messages.success(request,'email is taken')

        else:
            user = User(username=uname,email=email)
            user.set_password(passw)
            user.save()
            messages.success(request,'Account created !!')
            return redirect('/')



    return render(request,'create_account.html')
    
def login_handal(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        
        if not username or not  password:
            messages.success(request,'Both fields are required  !')

        user_obj = User.objects.filter(username=username).first()
        user = authenticate(username=username,password=password)

        if user_obj is None:
            messages.success(request,'User Not found !')
            print(user_obj)

        if user is not None:
            login(request,user)
            return redirect('/forms/')
                
        if user is None:
            messages.success(request,'Wrong Password !!')

    return render(request,'login.html')






    

