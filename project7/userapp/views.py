from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def userregister(request):
    return HttpResponse("this is views file inside the userapp")

def sample(request):
    return HttpResponse("hii this is sample function inside the userapp with response url.py file inside the user app")

def login(request):
    return render(request, 'userapp/login.html')

def register(request):
    return render(request, "userapp/register.html")

def indexregister(request):
    return render(request, "register.html")