
from django.shortcuts import render


def hellodjango(request):
    return render(request, "hi1.html")
