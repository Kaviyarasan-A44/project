from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    return HttpResponse('<h1> hello this is first</h1>')

def second_view(request):
    return HttpResponse('<h1> hello this is second</h1>')

def third_view(request):
    return HttpResponse('<h1> hello this is third</h1>')
