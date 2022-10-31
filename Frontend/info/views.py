from django.shortcuts import render
from .services import Services

# Create your views here.

#Pruebas
def Data(request):
    Data = Services.getData()
    
    result = ""
    if request.method == "POST":
        text = request.POST.get("text")
        result = Services.addData({'msg': text})
    
    return render(request, 'info.html', {'data': Data, 'result': result})

    