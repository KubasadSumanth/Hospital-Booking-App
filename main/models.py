from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todoList",null=True)

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class Hospitals(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todoList",null=True)

    hospitalName = models.CharField(max_length=200)
    specialities = models.CharField(max_length=200)
    noOfSeats = models.IntegerField()
    doctorName = models.CharField(max_length=1000)

    def __str__(self):
        return self.hospitalName
class Patients(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todoList",null=True)

    name = models.CharField(max_length=200)
    casestudydata = models.CharField(default=" ",max_length=2000)

    def __str__(self):
        return  " - "+ self.casestudydata

class Book(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todoList",null=True)
    hospitalName = models.CharField(default="No Name",max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    consulttext = models.CharField(max_length=200)
    doctorName = models.CharField(max_length=1000)

    def __str__(self):
        return self.username+" - "+self.consulttext