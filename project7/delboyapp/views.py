from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def carrydata(request, data):
    return HttpResponse(f'<h1>this is delboy app response this carry {data} to backend</h1>')
