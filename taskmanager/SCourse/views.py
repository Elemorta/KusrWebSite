from django.shortcuts import render, redirect
from .forms import AuthForm, Application as App
from .models import *

base = [{'title': 'Авторизация', 'url_name': 'auth'},
        {'title': 'Подключить пакет цифрового телевидения', 'url_name': 'application'},
        {'title': 'Тарифы', 'url_name': 'bundles'}]


def index(request):
    Citys = Town.objects.all()
    return render(request, 'main/about.html', {'Citys': Citys, 'base': base, 'title': 'Главная страница'})


def Authorization(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AuthForm()
    return render(request, 'main/OperatorInput.html', {'base': base, 'form': form, 'title': 'Авторизация'})


def Bundles(request):
    Bund = Bundle.objects.all()
    return render(request, 'main/Bundles.html', {'base': base, 'bundles': Bund, 'title': 'Тарифы'})


def application(request):
    if request.method == 'POST':
        form = App(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                form.save()
                return redirect('application')
            except:
                form.add_error(None, 'Ошибка отправки заявки')
    else:
        form = App()
    return render(request, 'main/Application.html', {'base': base, 'form': form, 'title': 'Подключение тарифа'})


def applicationBund(request, bundles_name):
    if request.method == 'POST':
        form = App(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                form.save()
                return redirect('application')
            except:
                form.add_error(None, 'Ошибка отправки заявки')
    else:
        form = App()
    bundle = bundles_name
    return render(request, 'main/Application.html', {'bundle': bundle, 'base': base, 'form': form, 'title': 'Подключение тарифа'})
