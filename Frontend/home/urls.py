from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('uploadConfigXml', views.uploadConfigXml),
    path('uploadConsumedXml', views.uploadConsumedXml),
    path('consultData', views.consultData),
    path('createResource', views.createResource),
    path('createCategory', views.createCategory),
    path('createConfig', views.createConfig),
    path('createClient', views.createClient),
    path('createInstance', views.createInstance)
]