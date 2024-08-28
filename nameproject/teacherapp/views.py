from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse





def student_name2(request):
    content='<h1>student name 2</h1>'
    return HttpResponse(content)


def student_mark2(request):
    content='<h1>student mark 2</h1>'
    return HttpResponse(content)

def student_rollno2(request):
    content='<h1>student rollno 2</h1>'
    return HttpResponse(content) 
