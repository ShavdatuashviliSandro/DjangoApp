from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, you are on mens side!')

def show(request, post_id):
    return render(request, 'men_hub/show.html', {'id': post_id})
