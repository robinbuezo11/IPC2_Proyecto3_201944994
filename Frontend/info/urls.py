from django.urls import path
from . import views

urlpatterns = [
    #Pruebas
    path('data', views.Data),
]