from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('auth/', views.Authorization, name='auth'),
    path('bundles/', views.Bundles, name='bundles'),
    path('application/', views.application, name='application'),
    path('aplicationbundles/<slug:bundles_name>/', views.applicationBund, name='appbund')
]