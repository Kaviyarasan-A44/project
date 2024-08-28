from django.shortcuts import render
from django.http import Httpresponse

# Create your views here.
def display(request):
    content='<h1>welcome to django </h1>'
    return Httpresponse(content)
