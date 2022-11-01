from django.urls import path
from . import views

urlpatterns = [
    #Pruebas
    path('', views.welcome),
    path('uploadFile', views.uploadFile)
]