from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def home_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your message has been saved')
    else:
        form = ContactForm()

    return render(request, 'staffice/index.html', {'form': form})
