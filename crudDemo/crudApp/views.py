from django.shortcuts import render,redirect
from crudApp.models import Employee
from crudApp.forms import EmployeeForm

def retrieve_view(request):
    employees = Employee.objects.all()

    return render(request,'crudApp/index.html',{'employees':employees})

def create_view(request):
    employees = EmployeeForm()
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/display')

    return render(request,'crudApp/create.html',{'employees':employees})



def delete_view(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/display')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method =="POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/display')

    return render(request,'crudApp/update.html',{'employee':employee})









