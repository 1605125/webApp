from django.shortcuts import render
from formapp.forms import FormExample


def formExample(request):
    form = FormExample()
    d1 ={
        'form': form
    }
    return render(request, 'form.html', d1)