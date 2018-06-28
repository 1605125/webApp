from django.shortcuts import render


def helloCompany(request):
    mydictionary = {
        'Name': 'Megha',
        'email': 'meghagupt@hello.com ',
        'List1': [1, 2, 3, 4, 5, 6],
        'dict1': {'city': 'Bangalore', 'street': 'BTM'}
    }
    return render(request, 'company.html', mydictionary)
