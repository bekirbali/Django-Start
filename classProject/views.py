from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World This is views</h1>")

def goodbye(request):
    return HttpResponse("<h1>Goodbye World</h1>")