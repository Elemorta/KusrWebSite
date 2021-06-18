from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from .forms import Application as App
from .models import *

base = [{'title': 'Подключить пакет цифрового телевидения', 'url_name': 'application'},
        {'title': 'Тарифы', 'url_name': 'bundles'},
        {'title': 'Авторизация', 'url_name': 'auth'}]


class Mainpage(ListView):
    queryset = {'base': base}
    template_name = 'main/about.html'
    extra_context = {'title': 'О нас'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base'] = base
        return context


class Authorization(LoginView):
    queryset = {'base': base}
    template_name = 'main/SignIn.html'
    form_class = AuthenticationForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base'] = base
        return context

    def get_success_url(self):
        return reverse_lazy('operatormenu')


class OperatorMenu(ListView):
    queryset = {'base': base}
    template_name = 'main/OperatorMenu.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base'] = base
        return context


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

def page404(request):
    return render(request, 'main/404.html', {'base': base})
