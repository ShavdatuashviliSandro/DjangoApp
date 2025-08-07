from django.shortcuts import render
from contact.models import Contact

def create(request):
    if request.method == 'POST':
        Contact.objects.create(name=request.POST['name'], email=request.POST['email'], message=request.POST['message'])
        return render(request, 'create.html', {'a': 1})
    else:
        return render(request, 'create.html', {'a': 1})
