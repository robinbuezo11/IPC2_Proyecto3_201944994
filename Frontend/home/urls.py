from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('uploadConfigXml', views.uploadConfigXml),
    path('uploadConsumedXml', views.uploadConsumedXml)
]