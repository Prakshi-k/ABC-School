from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class student_manager(models.Manager):
    def sort_id(x):
        return super().order_by('stuid').all()

class student(models.Model):
    stuid=models.IntegerField()
    rollno=models.IntegerField()
    fname=models.CharField(max_length=200)
    mname=models.CharField(max_length=200)
    lname=models.CharField(max_length=250)
    dob=models.CharField(max_length=20)
    mobno=models.CharField(max_length=10)
    add=models.CharField(max_length=500)
    std=models.IntegerField()

    objects=models.Manager()

    stud_manager=student_manager()


class contactnow(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    email=models.EmailField(max_length=250)
    message=models.CharField(max_length=500)

    object=models.Manager()

class teacher(models.Model):
    fname=models.CharField(max_length=200)
    mname=models.CharField(max_length=200)
    lname=models.CharField(max_length=250)
    dob=models.CharField(max_length=20)
    mobno=models.CharField(max_length=10)
    add=models.CharField(max_length=500)
   
class staff(models.Model):
    fname=models.CharField(max_length=200)
    mname=models.CharField(max_length=200)
    lname=models.CharField(max_length=250)
    dob=models.CharField(max_length=20, null=True )
    mobno=models.CharField(max_length=10 , null=True )
    add=models.CharField(max_length=500, null=True )
   


class kindergarten(models.Model):
    stuid=models.IntegerField()
    rollno=models.IntegerField()
    fname=models.CharField(max_length=200)
    mname=models.CharField(max_length=200)
    lname=models.CharField(max_length=250)
    dob=models.CharField(max_length=20)
    mobno=models.CharField(max_length=10)
    add=models.CharField(max_length=500)
    section=models.CharField(max_length=2)

    object_kg=models.Manager()



