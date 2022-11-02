from django.shortcuts import render
from django.http import HttpResponse
from .services import Services

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def uploadConfigXml(requests):
    if requests.method == 'POST' and requests.FILES['myfile']:
        myfile = requests.FILES['myfile']
        result = Services.uploadConfigXml(myfile)
        return render(requests, 'uploadConfigXml.html', {'result': result})
    return render(requests, 'uploadConfigXml.html')

def uploadConsumedXml(requests):
    if requests.method == 'POST' and requests.FILES['myfile']:
        myfile = requests.FILES['myfile']
        result = Services.uploadConsumedXml(myfile)
        return render(requests, 'uploadConsumedXml.html', {'result': result})
    return render(requests, 'uploadConsumedXml.html')