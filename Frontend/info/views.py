from django.shortcuts import render
from .services import Services

# Create your views here.

#Pruebas
def Data(requests):
    Data = Services.getData()
    
    result = ""
    if requests.method == "POST":
        text = requests.POST.get("text")
        result = Services.addData({'text': text})
    
    return render(requests, 'info.html', {'data': Data, 'result': result})

    