from django import forms
import django
from django.db import models
from django.forms import fields
from django.forms.models import ModelForm
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model =   models.Employee
        fields = ('fullname','emp_code','mobile','position')

        labels = {
            'fullname' : 'Full Name',
            'emp_code' : 'EmpCode',
            'mobile' : 'Mobile',
            'position' : 'Position',


        }
        # fields = '__all__'
        # fields = {'fullname','emp_code','mobile','position'}

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False
        self.fields['fullname'].required = False
        self.fields['mobile'].required = False
        self.fields['position'].required = False


            # for visible in self.visible_fields():
            #     visible.field.widget.attrs['class'] = 'form-control'




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']