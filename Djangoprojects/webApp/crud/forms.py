from django import forms
from crud.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        # OR
        fields = ('emp_email', 'address', 'phone')
