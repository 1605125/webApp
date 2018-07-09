from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm  # default way of getting login page
from django.contrib.auth.models import User
from sites.forms import LoginForm


def userLogin(request):  # we have to design form for login
    if request.user.username:
        return redirect(userDashBoard)
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username,
                password=password
            )
            if user is None:
                message = "User not found!"
            else:
                login(request, user)
                return redirect(userDashBoard)
    return render(
        request,
        'sites/login.html',
        {
            'form': form,
            'msg': message
        }
    )


def userDashBoard(request):
    return render(request, 'sites/dashboard.html')


def userLogout(request):
    logout(request)
    return redirect(userLogin)


def userRegistration(request):
    form = UserCreationForm()
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # password1 is of main django framework go to UserCreation
            # and you will get another  file
            user.username = username
            user.set_password(password)  # password has key this method will generate has key password in form of string
            # user.password = password # raw password
            user.save()
            message = 'Registration done successfully'

    return render(
        request,
        'sites/registration.html',
        {'form': form, 'msg': message}
    )
