from django.shortcuts import render


def Companyapp(request):
    myDic={
        'name': 'Megha Gupta',
        'list': [8, 'hi', 9, 'hello'],
        'street': "Btm",
        'myss': {'nice': 'girl', 1: 'nn'}
    }
    return render(request, 'company.html', myDic)