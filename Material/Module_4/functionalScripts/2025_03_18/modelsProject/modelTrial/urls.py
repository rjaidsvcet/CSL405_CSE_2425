from django.urls import path
from .views import dataRetrieval

urlpatterns = [
    path ('', dataRetrieval, name='dataRetrieval')
]