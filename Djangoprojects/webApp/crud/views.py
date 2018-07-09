from django.shortcuts import render, redirect
from crud.forms import EmployeeForm
from crud.models import Employee
from django.contrib.auth.decorators import login_required


def create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp = Employee()  # saving database in reference of model
            empName = form.cleaned_data['emp_email'].split('@')[0]
            emp.emp_name = empName
            emp.emp_email = form.cleaned_data['emp_email']
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            # emp.pincode = form.cleaned_data['pincode']
            emp.save()
            return redirect(index)

            # form.save()
    return render(request, 'crud/create.html', {'form': form})


@login_required(login_url='/sites/signin') # takes to sigin page
def index(request):
    # resultSet = Employee.objects.filter()  # it is like select * from table
    # resultSet = Employee.objects.filter(emp_name='ajit').order_by('-id')  # it is like select * from table
    # resultSet = Employee.objects.filter(emp_name='ajit').values('id', 'emp_name')  # it is like select * from table
    resultSet = Employee.objects.raw("select * from employee")  # it is like select * from table
    # resultSet = Employee.objects.filter(emp_name='ajit').order_by('-id')  # it is like select * from table

    return render(request, 'crud/index.html', {'data': resultSet})


def update(request, id):
    # def update(request, id, name):

    data = Employee.objects.get(id=id)
    # select * from employee where id = id
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)  # read value from data and it will map with form object
        if form.is_valid():
            emp = Employee()  # saving database in reference of model
            emp.id = id
            empName = form.cleaned_data['emp_email'].split('@')[0]
            emp.emp_name = empName
            emp.emp_email = form.cleaned_data['emp_email']
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            # emp.pincode = form.cleaned_data['pincode']
            emp.save()
            return redirect(index)

            # form.save()
    return render(request, 'crud/update.html', {'form': form})


def view(request, id):
    data = Employee.objects.get(id=id)
    return render(request, 'crud/view.html', {'data': data})


def delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect(index)
