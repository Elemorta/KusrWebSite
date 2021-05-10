from django.shortcuts import render
from .models import Town


def index(request):
    Citys = Town.objects.all()
    return render(request, 'main/Application.html')

def OperatorAuth(request):
    return render(request, 'OperatorInput')