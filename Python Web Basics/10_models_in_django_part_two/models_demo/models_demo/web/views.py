from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from models_demo.web.models import Employee, Department


# Create your views here.
def home_page(request):
    # x = list(Employee.objects.all())
    # print(x)
    # print(list(User.objects.all()))
    # print((list(Department.objects.all())))
    #
    # employees = Employee.objects.all()
    # employees_list = list(employees)
    # print(employees)  # QuerySet lazy structure
    # print(employees_list)  # list

    context = {
        'employees': [e for e in Employee.objects.all() if e.department_id == 1],
        'employees2': Employee.objects.filter(department_id=1).order_by('last_name', 'first_name'),
        'department': Department.objects.get(pk=1),
        'employees3': Employee.objects.filter(department__name='Engineering')
    }
    # get returns an object,and is eager not return a QuerySet NOT LAZY
    # get returns a single object and throws error when none or multiple resultS

    return render(request, 'web/index.html', context)


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug),
    }

    return render(request, 'web/department-details.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()

    return redirect('index')
