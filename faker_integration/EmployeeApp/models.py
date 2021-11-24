from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField()
    efnm = models.CharField(max_length=20)
    elnm = models.CharField(max_length=20)
    edob = models.DateField()
    email = models.EmailField(max_length=30)
    eaddr = models.TextField()
    ephone = models.BigIntegerField()