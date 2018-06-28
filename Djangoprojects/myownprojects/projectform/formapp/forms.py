from django import forms


class FormExample(forms.Form):
    emp_name = forms.CharField(min_length=8, max_length=20, label='Name')
    email = forms.EmailField()
    address = forms.CharField(max_length=250)
