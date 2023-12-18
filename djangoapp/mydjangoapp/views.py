from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def index(request):
    mymodels = MyModel.objects.all()
    output = ', '.join([m.name for m in mymodels])
    return HttpResponse(output)