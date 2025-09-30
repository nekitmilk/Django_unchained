from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template


def home(request):
    return render(request, 'templates/index.html')

def my_template(request):
    return render(request, 'templates/static_handler.html')

def my_home(request):
    return HttpResponse(u'Привет, Мир!')

# Create your views here.
