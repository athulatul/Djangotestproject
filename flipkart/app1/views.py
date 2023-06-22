from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.



def index(request):
    return HttpResponse("Hi Dears")



def test_fun(request):
    return render(request, 'test.html')



def test_fun2(request):
    return render(request, 'test2.html')



def test_fun3(request):
    return render(request, 'test3.html')





























