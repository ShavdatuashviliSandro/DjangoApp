from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("show/<int:post_id>", views.show, name='show'),
]
