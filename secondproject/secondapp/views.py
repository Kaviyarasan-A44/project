from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def display_morning(request):
    content='<h1> good morning</h1>'
    return HttpResponse(content)

def display_evening(request):
    content='<h1> good evening</h1>'
    return HttpResponse(content)
