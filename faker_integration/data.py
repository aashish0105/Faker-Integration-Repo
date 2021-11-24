import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','faker_integration.settings')
django.setup()
from EmployeeApp.models import *
from faker import Faker
from random import *

fake=Faker()

def phone():
    f = str(randint(6,9))
    for i in range(9):
        f = f + str(randint(6,9))
    return int(f)

def populate(n):
    for i in range(n):
        eid = fake.random_int(min=1,max=100)
        efnm = fake.first_name()
        elnm = fake.last_name()
        edob = fake.date()
        email = fake.email()
        eaddr = fake.address()
        ephone = phone()
        obj = Employee.objects.get_or_create(eid=eid,efnm=efnm,elnm=elnm,edob=edob,email=email,eaddr=eaddr,ephone=ephone)


populate(20)