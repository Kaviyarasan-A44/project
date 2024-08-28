from django.shortcuts import render
import datetime

# Create your views here.
def greet(request):
    date=datetime.datetime.now()
    my_data = {'today':date,'name':'kavi','ug':'bca','nationality':'indian'}
    return render(request, 'templateapp/template1.html',context=my_data)
