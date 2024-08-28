from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def student_name(request):
    content='<h1>student name</h1>'
    return HttpResponse(content)


def student_mark(request):
    content='<h1>student mark</h1>'
    return HttpResponse(content)

def student_rollno(request):
    content='<h1>student rollno</h1>'
    return HttpResponse(content)    
