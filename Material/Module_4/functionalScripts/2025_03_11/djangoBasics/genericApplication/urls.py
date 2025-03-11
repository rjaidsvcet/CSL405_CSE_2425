from django.urls import path
from . import views

urlpatterns = [
    # path ('', views.basicResponse, name='response'),
    # path ('webpage/', views.basicWebpage, name='webpage'),
    # path ('another/', views.anotherPage, name='another')
    path ('', views.forms, name='forms'),
    path ('result/', views.result, name='result')
]