from django.core.exceptions import ValidationError
from django.shortcuts import render
from contact.models import Contact

def create(request):
    if request.method == 'POST':

        contact = Contact(name=request.POST.get('name', '').strip(),
                          email=request.POST.get('email', '').strip(),
                          message=request.POST.get('message', '').strip())
        try:
            contact.full_clean()
            contact.save()
            return render(request, 'create.html')
        except ValidationError as e:
            return render(request, 'create.html',
                          {'errors': e})

    return render(request, 'create.html')
