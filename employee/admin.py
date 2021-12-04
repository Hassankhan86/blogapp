from django.contrib import admin
import employee

# Register your models here.

from employee.models import Employee 

# admin.site.register(Postion)
admin.site.register(Employee)