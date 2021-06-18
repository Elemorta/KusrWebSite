from django.urls import path
from . import views


urlpatterns = [
    path('', views.Mainpage.as_view(), name='home'),
    path('auth/', views.Authorization.as_view(), name='auth'),
    path('bundles/', views.Bundles, name='bundles'),
    path('application/', views.application, name='application'),
    path('operatormenu/,', views.OperatorMenu.as_view(), name = 'operatormenu'),
    path('aplicationbundles/<slug:bundles_name>/', views.applicationBund, name='appbund'),
    path('404page/', views.page404, name='page404')
]