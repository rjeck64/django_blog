from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def user(request):
    user = User.objects.all()
    return render(request, "user.html", {'users' : user})