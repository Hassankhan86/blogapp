from django import forms
from django.shortcuts import redirect, render
import employee

from employee.forms import EmployeeForm
# from employee.models import Employee
from .forms import EmployeeForm,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import Employee

@login_required(login_url='login')
def employee_list(request,):

    # if request.user.is_authenticated:
        # obb = request.user.id
        # print('obb :  ',obb)
        # # ob = Employee.objects.filter(user =request.user).first()
        # pp = Employee.objects.filter(user=request.user)
        # print(pp)

        # ob = Employee.objects.filter(id=id)

        # ob = request.user.Employee()
        # print('ObBB',ob)
        # context = {"employee_list":ob,}

    #     ob = Employee.objects.get(user= request.user)
    #     # ob1 = Employee.objects.all()
    #     # print("Ob111",ob)
    #     context = {"employee_list1":ob,}

    # # emp = request.user.Employee.all()
    # else:
    # employee1 = Employee.objects.get(id=id)
    # print('Employee : ', employee1.position)
    employee = Employee.objects.all()
    # obj = Employee.objects.filter(user=request.user)
    # customers = Employee.objects.filter(user=request.user)
    # cust = Employee.objects.get(user = request.user)
    # print(obj)
    # print(customers)
    # print(cust)
    # id    = request.user.id
    # detail = Employee.objects.filter(id=id)
    # id = request.user.id
    # detail = Employee.objects.filter(id=id)
    # print("detail_mobile : ",id )
    # aa = request.user.Employee(user=id)
    # aa  = Employee.objects.filter(id  = id)

    # print('aa : ',detail)

    # current_user = request.user
    # print(current_user.id)
    # id = request.user.id
    # print(id)
    # ob= Employee.objects.filter(user=request.user)
    # print('team',ob.mobile)
    # print(ob)
    # ob = Employee.objects.get(id=pk_test)

    # ob = Employee.objects.filter(id=id)
    # print("Ob111",ob)
    # print('-------------------------')
    # id = request.user.id
    # detail = Employee.objects.filter(user=id)
    # print("Ob111",id)
    # print("Ob111",detail)

    # current_user = request.user

    # oo = Employee.objects.get(user=request.user)
    # print('oo : ',oo.mobile)
    # user_id = current_user.id
    # print('current_user : ',current_user)
    # print('user_id : ',user_id)
    print('-------------------------')
    # detail = Employee.objects.filter(user=request.user)
    # print('detail : ', detail)
    id11 = request.user
    # profile = Employee.objects.create(user=request.user)
    # print('id1234123 : ',profile)

    print('id : ',id11)
    if request.method == 'POST':
        # form = forms.addProfilepic(request.POST, request.FILES)
        # if form.is_valid():
        #     obj = Employee.objects.filter(user=request.user).first()
        #     r = form.save()
            print("---------- 1st")

            # obj.profile_pic = request.FILES['picture'].name

            print("----------")
            # obj.save()
            return employee_list(request)
    else:
        # print("AASD")
        detail = Employee.objects.filter(user=id11)
        print('dddd 123412 : ',detail)
        status_list = Employee.objects.filter(user=request.user)
        # print('asd123 : ',status_list)

        SS = Employee.objects.filter(user=request.user)
        # print('SS ; ',SS)
    print('-------------------------')

    context = {"user1":detail,"employee_list":SS}

    return render(request,'employee/employee_list.html',context)


@login_required(login_url='login')
def employee_form(request,id=0):
    # dd = request.user.id
    # print(dd)
    # print('Employee : ', employee1.position)
    id = request.user.id

    if request.method == 'POST':
        emp = Employee()
        # emp.save()
        name = request.POST.get('fullname')
        mob = request.POST.get('mobile')
        em_code = request.POST.get('emp_code')
        pos = request.POST.get('position')

        print(name)
        print(mob)
        print(em_code)
        print(pos)

        emp.fullname = name
        emp.mobile = mob
        emp.emp_code = em_code
        emp.position = pos

        emp.save()

        # emp.user.add(request.user)

        emp.user = request.user
        emp.save()

    EMp1 = Employee()
    print('------------------------')
    # form = EmployeeForm()
    # if request.method == 'POST':
    #     # employee1 = Employee.objects.filter(id=id)
    #
    #     form = EmployeeForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/list',)
            
    # context = {'form':EMp1,}
    print('------------------------')
    return render(request,'employee/employee_form.html',)

    # if request.method == "GET":

    #     if id==0:
            
    #         form = EmployeeForm
    #     else:
    #         employee = Employee.objects.get(pk=id)
    #         form = EmployeeForm(instance = employee)

        # return render(request,'employee/employee_form.html',{'form':form})
    # else:
    #     if id == 0:

    #         form = EmployeeForm(request.POST)
    #     else:
    #         employee = Employee.objects.get(pk=id)
    #         form = EmployeeForm(request.POST,instance=employee)
    #     if form.is_valid():
    #         form.save()

    #     return redirect('/list')

def update_emp(request,pk):
    print('------------------------')

    employee = Employee.objects.get(id=pk)
    print('Employee : ',employee.position)

    form = EmployeeForm(instance = employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid():
            form.save()
            return redirect('/list')

    context = {'form':form}
    print('------------------------')

    return render(request,'employee/update_form.html',context)

def employee_delete(request,pk):

    # emp = Employee.objects.get(pk=id)
    # emp.delete()
    

    # return redirect('/list')

    emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        emp.delete()

        return redirect('/list')

    context = {'item':emp}

    return render(request,'employee/employee_delete.html',context)

def logout_page(request):
    # return redirect('dashboard:dashboard_view')
    # logout(request)
    # return login(request)
    # return redirect('logout/')

    logout(request)
    return  redirect('login')

def login_page(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            print(user)
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('/list')
    else:

        form = AuthenticationForm()
    # if request.user.is_authenticated:
    #     return redirect('/list')
    # else:
    #     if request.method == 'POST':
    #         username = request.POST.get('username')
    #         password = request.POST.get('password')
    #
    #
    #         user = authenticate(request,username=username,password=password)
    #
    #         if user is not None:
    #             login(request,user)
    #             return redirect('/list')
    #         else:
    #             messages.info(request,"Username Or Password is Incorrect ")

    #  if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         # log the user in
    #         user = form.get_user()
    #         login(request, user)

    #         if 'next' in request.POST:
    #             return redirect(request.POST.get('next'))
    #         return redirect('dashboard:dashboard_view')
    #         # return HttpResponse("yes")
    # else:
    #     form = AuthenticationForm()
    return render(request,'employee/login_page.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/list')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                # user = form.save()
                username = form.cleaned_data.get('username')
                Employee.objects.create(
                    user = user,
                    fullname=username,
                )
                messages.success(request, 'Account was Successfully created for ' + username)
                return redirect('login')

    #         group = Group.objects.get(name='client')
    #         user.groups.add(group)

            # a = Employee(user = username)
            # a.save()

            # group = Group.objects.get

            # a = Employee(user = users)
            # Employee.user = users
            # a.user =  users
            # a.save()
            
    context = {'form':form}
    return render(request,'employee/register_page.html',context)