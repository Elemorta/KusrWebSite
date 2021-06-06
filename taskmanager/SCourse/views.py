from django.shortcuts import render
from .models import *

base = {'Авторизация', 'Подключить пакет цифрового телевидения', 'Тарифы'}


def index(request):
    Citys = Town.objects.all()
    return render(request, 'main/Application.html', {'Citys': Citys, 'Base': base})


def OperatorAuth(request):
    return render(request, 'main/OperatorInput.html', {'Base': base})


def Bundles(request):
    Bundles = Bundle.objects.all()
    return render(request, 'main/Bundles.html', {'Base': base, 'bundles': Bundles})


