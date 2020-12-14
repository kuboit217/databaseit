from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.

#trang home
def home(request):
    context = {}
    return render(request, 'requestit/home.html', context)