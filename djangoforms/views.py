from django.shortcuts import render
from .forms import Contactform


def contact(request):
    if request == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = Contactform()
    return render(request, 'contact.html', {'form': form})
