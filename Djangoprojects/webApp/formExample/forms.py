from django import forms  # predefined library
from django.core.validators import ValidationError


class FormExample(forms.Form):  # inheritance

    emp_name = forms.CharField(
        min_length=8, max_length=20,
        required=True,
        label='Employee Name',
        help_text='please provide valid user name',
        error_messages={
            'required': "Employee name cannot be blank",
            'min_length': 'new text'
        },
        widget=forms.TextInput(
            attrs={
                'placeholder': "Employee name..",
                'class': 'test',
                'id': 'fdfdsts'
            }
        )

    )
    email = forms.EmailField()
    is_active = forms.BooleanField(required=False)
    active = forms.CharField(
        widget=forms.CheckboxInput,
        required=False
    )

    gn = (
        ('m', "Male"),
        ('f', 'Female')

    )

    gender = forms.ChoiceField(
        choices=gn,
        widget=forms.RadioSelect
    )
    password1 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput,
        label='Create password'
    )
    password2 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput,
        label='confirm password'
    )
    cityList = (
        ('', '--Select optioin'),
        ('chennai', "Chennai"),
        ('bangalore', 'Bangalore'),
        ("hyderabad", 'Hyderabad'),
        ("mysore", 'Mysore')

    )

    city = forms.ChoiceField(
        choices=cityList
    )

    address = forms.CharField(
        max_length=250,
        widget=forms.Textarea
    )

    def clean(self):
        form_data = self.cleaned_data
        if 'emp_name' in form_data:
            if form_data['emp_name'].isdigit():
                self.errors['emp_name'] = ["Employee name cannot be digits"]

        if 'email' in form_data:
            if form_data['email'].find("@mytectra.com") < 0:
                self.errors['email'] = ["Inavlid Email"]

        if 'password1' in form_data and 'password2' in form_data:
            if form_data['password1'] != form_data['password2']:
                self.errors['password2'] = ['password mistach']

        return form_data
