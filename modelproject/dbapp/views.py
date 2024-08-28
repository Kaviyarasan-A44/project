from django.shortcuts import render
from dbapp.models import student
# Create your views here.

def display_stu_data(request):
    student_list=student.objects.all()
    stu_data_dict={'student_list':student_list}
    return render(request,"dbapp/index.html",stu_data_dict)
