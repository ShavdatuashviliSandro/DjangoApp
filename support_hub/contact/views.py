from django.shortcuts import render
from contact.models import Contact
from .forms import ContactForm

def create(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        Contact.objects.create(name=request.POST.get('name', '').strip(),
                               email=request.POST.get('email', '').strip(),
                               message=request.POST.get('message', '').strip())

        return render(request, 'create.html', {'form': ContactForm()})
    return render(request, 'create.html', {'form': form})
