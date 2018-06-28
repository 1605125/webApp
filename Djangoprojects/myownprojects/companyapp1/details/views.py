from django.shortcuts import render

def bio_data(request):
    return render(request, 'biodata.html')