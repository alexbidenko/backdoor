from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ideas/<str:date_start>/<str:date_end>', views.ideas, name='ideas'),
    path('create', views.create, name='create'),
    path('command', views.command, name='command'),
]
