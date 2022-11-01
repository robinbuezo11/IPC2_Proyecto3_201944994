from django.shortcuts import render
from django.http import HttpResponse
from .services import Services

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def uploadFile(requests):
    if requests.method == 'POST' and requests.FILES['myfile']:
        myfile = requests.FILES['myfile']
        result = Services.uploadXml(myfile)
        return render(requests, 'uploadfile.html', {'result': result})
    return render(requests, 'uploadfile.html')