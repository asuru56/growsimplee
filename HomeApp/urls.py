from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainHome, name='MainHome'),
    path('temp1_navbar/', views.navbar_fun, name='navbar'),
]
