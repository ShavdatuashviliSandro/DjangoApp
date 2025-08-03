from django.shortcuts import render
from django.templatetags.static import static


def index(request):
    logo_url = static('images/heart.svg')

    return render(request, 'main/index.html', {'range': range(5), 'logo_url': logo_url, 'id': 1})

def show(request, post_id):
    return render(request, 'main/show.html', {'post_id': post_id})
