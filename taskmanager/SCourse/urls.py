from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('operator', views.OperatorAuth),
    path('bundles', views.Bundles)
]