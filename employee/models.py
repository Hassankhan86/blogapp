from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Postion(models.Model):
#     title = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.title

class Employee(models.Model):
    user =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=105)
    position = models.CharField(max_length=105)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.fullname