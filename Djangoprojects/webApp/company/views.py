from django.shortcuts import render


def helloCompany(request):
    myDictionary = {
        'name': 'Megha',
        'email': 'rag@gmail.com',
        'list1': [1, 2, 3, 4],
        'dict2': {'city': 'Bangalore', 'address': 'Mysore'}
    }
    return render(request, 'company.html', myDictionary)
