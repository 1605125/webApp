from django.shortcuts import render


# Create your views here.
def helloDjango(request):
    return render(request, 'loginapp.html')