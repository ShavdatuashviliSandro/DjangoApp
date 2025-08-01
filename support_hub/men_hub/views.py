from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, you are on mens side!')

def show(request, post_id):
    return HttpResponse(f"This is a post with ID {post_id}!")
