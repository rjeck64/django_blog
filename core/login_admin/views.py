from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         email = form.cleaned_data['email']
         password = form.cleaned_data['password']
         confirm_password = form.cleaned_data['confirm_password']

         if password == confirm_password:
            User.objects.create_user(username=username,email=email,password=password)
            messages.success(request,"Register Berhasil, Silahkan Login")
            return redirect('register')
         else:
            messages.error(request,"password tidak sama")
            return render(request,'register.html' , {'form' : form})
    else:
        form = RegisterForm()
        return render(request,'register.html' , {'form' : form})

def login_admin(request):
   if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         password = form.cleaned_data['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('dashboard')
         else:
             messages.error(request, 'Username atau password salah. Silakan coba lagi.')
             return render(request, 'login.html', {'form': form})
   else:
      form = LoginForm()
      return render(request, 'login.html', {'form': form})
   
def logout_user(request):
   logout(request)
   return redirect('login')