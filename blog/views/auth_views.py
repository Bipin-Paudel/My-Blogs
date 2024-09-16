from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from django.contrib import messages


def renderRegisterForm(request):
    if request.method =='POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/blog/register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect('/blog/register')
        user =User.objects.create(
         username=username,
         email=email,
         
        ) 
        print(User)
        user.set_password(password)
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('/blog/login')

    else:    
       return render(request,'auth/register.html')

def renderLoginForm(request):
   if request.method =='POST':
      email = request.POST['email']
      password =request.POST['password']
      user = authenticate(request, email=email, password=password )
      print(email, password, user)
      if user is not None:
        login(request,user)
        
        return redirect('/')
        
      else:
        messages.error(request,"Invalid email or password")
        print('hello world')
        return redirect('/blog/login')
   else:  
      return render(request,'auth/login.html')
