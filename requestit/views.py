from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .decorators import unauthenticated_user, allowed_users , andmin_only

#trang home
@login_required(login_url='login')
@andmin_only
def home(request):
    context = {}
    return render(request, 'requestit/home.html', context)

#trang đăng nhập

def loginPage(request):
    context = {}
    return render(request, 'requestit/login.html', context)

#trang đăng ký
def registerPage(request):
    context = {}
    return render(request, 'requestit/register.html', context)