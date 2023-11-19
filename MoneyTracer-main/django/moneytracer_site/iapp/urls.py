from django.urls import path
from . import views

urlpatterns = [
    path('', views.iapp_home, name='iapp_home'),
    path('create', views.create, name='create'),
    path('./reg.html', views.create, name='reg')
]
