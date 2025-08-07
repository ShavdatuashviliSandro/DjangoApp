from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'a': 1})

def create(request):
    return 1
