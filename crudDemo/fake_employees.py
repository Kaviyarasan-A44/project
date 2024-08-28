import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudDemo.settings')

import django
django.setup()

from crudApp.models import *
from faker import Faker
from random import *

faker = Faker()

def generate(num):
    for i in range(num):
        feNo = randint(101,1000)
        feName = faker.name()
        feSalary = randint(20001,50001)
        feAddress = faker.city()
        emp_record = Employee.objects.get_or_create(eNo=feNo,eName=feName, eSalary=feSalary, eAddress = feAddress)

generate(10)










