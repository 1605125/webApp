from django.shortcuts import render
from formExample.forms import FormExample


def formExample(request):   # class name and function not be same
    # print(request.method)
    # print(request.GET['name'])
    form = FormExample()
    if request.method == 'POST':
        form = FormExample(request.POST)
        if form.is_valid():
            pass

    d1 = {'form': form}
    return render(request, 'form_example.html', d1)  # d1 is pass input in html
