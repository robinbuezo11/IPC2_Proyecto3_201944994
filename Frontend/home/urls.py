from django.urls import path
from . import views

urlpatterns = [
    #Pruebas
    path('welcome', views.welcome),
    path('welcomeTemplate', views.welcomeTemplate)
]