#dojo/views.py
from django.shortcuts import render
from django.http import HttpResponse

def mysum(request, numbers):
    # result=sum(map(int,numbers.split("/")));
    result=sum(map(lambda s:int(s or 0),numbers.split("/")));
    return HttpResponse(result)
# Create your views here.
