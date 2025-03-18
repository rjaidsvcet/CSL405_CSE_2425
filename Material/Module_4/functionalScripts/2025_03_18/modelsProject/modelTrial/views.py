from django.shortcuts import render
from .models import Firstname

# Create your views here.
def dataRetrieval (request):
    firstname = Firstname.objects.all ()
    return render (request, 'index.html', {'name' : firstname})