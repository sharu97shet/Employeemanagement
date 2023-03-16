from django.shortcuts import render, HttpResponse, redirect
from .models import Department, Emp
from datetime import datetime


from django.db.models import Q

# from .models import Department

# Create your views here.


def emp(request):
    # return HttpResponse("Hello, world  !")

    return render(request, 'index.html')


def addEmployee(request):

    if request.method == 'POST':

        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        dept = request.POST['dept']
        salary = request.POST['salary']
        age = request.POST['age']
        hiredate = request.POST['hiredate']
        price = request.POST['price']
        img = request.POST['empimg']

        emprecord = Emp(
            firstname=firstname, lastname=lastname,  salary=salary, age=age, hiredate=datetime.now(), Image=img, price=price, dept_id=dept)
        emprecord.save()

        ID = emprecord.id

        print('record employee insert', ID)

        return HttpResponse("yes emp data is", ID)

    else:

        Deptecords = Department.objects.all()

        return render(request, 'addemp.html', {'dempdetails': Deptecords})


def viewEmployee(request):

    Employeerecords = Emp.objects.all()

    listofemp = [Employeerecords]

    print(listofemp)

    return render(request, 'viewemp.html', {'empdetails': Employeerecords})


def editEmployee(request):

    EMPiddd = request.GET['query']

    EmployeerecordsData = Emp.objects.get(id=EMPiddd)

    EmployeerecordsData2 = Emp.objects.values_list('Image')

    Employeerecords = Emp.objects.values_list('Image')

    listofemp = [EmployeerecordsData]
    print(EmployeerecordsData)

    print(EmployeerecordsData2)

    context = {
        'oneempdata': EmployeerecordsData
    }

    return render(request, 'editemp.html', context)


def UPDATE(request, id):

    if request.method == 'POST':

        # EMPiddd = request.POST['empid']

        # print(EMPiddd)

        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        dept = request.POST['dept']
        salary = request.POST['salary']
        age = request.POST['age']
        hiredate = request.POST['hiredate']
        price = request.POST['price']

        emprecord = Emp(
            id=id, firstname=firstname, lastname=lastname,  salary=salary, age=age, hiredate=datetime.now(),  price=price, dept_id=1)
        emprecord.save()

        # return render(request, ' viewemp.html')

        # EmployeerecordsData.firstname = firstname
        # EmployeerecordsData.lastname = lastname
        # EmployeerecordsData.salary = salary
        # EmployeerecordsData.age = age
        # EmployeerecordsData.price = price

        # EmployeerecordsData.save()

        # print('record employee updated')

        # return HttpResponse("PLEASE update   EMPLOYEE ! ", empId)

        return redirect('viewEmployee')


def rememp(request, emp_id=0):

    if emp_id:
        try:
            emp_to_remove = Emp.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("EMPLOYEE  REMOVED SUCCESSFULLY  !")
        except:
            return HttpResponse("PLEASE ENTER VALID EMPLOYEE !")

    Employeerecords = Emp.objects.all()

    context = {
        'emp': Employeerecords
    }

    return render(request, 'removeemp.html', context)


def filter(request):
    Departmentrecords = Department.objects.all()

    context = {
        'emp': Departmentrecords
    }

    if request.method == 'POST':

        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        dept = request.POST['dept']

        Employeerecords = Emp.objects.all()

        if firstname != '':
            Employeerecords = Employeerecords.filter(
                Q(firstname=firstname) | Q(lastname=lastname))

        context2 = {
            'empdetails': Employeerecords
        }
        return render(request, 'viewemp.html', context2)

    elif request.method == '':

        return HttpResponse("please submit details for , filter  !")
    else:
        return render(request, 'filteremp.html', context)

    # return HttpResponse("add , filter  !")
