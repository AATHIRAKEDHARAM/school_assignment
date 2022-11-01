from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class AdminReg(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    dob=models.DateField()
    image=models.ImageField(upload_to="img/")
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    class Meta:
        db_table="admin_reg"



class StudentReg(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    dob=models.DateField()
    image=models.ImageField(upload_to="student_img/")
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


    class Meta:
        db_table="student_reg"

