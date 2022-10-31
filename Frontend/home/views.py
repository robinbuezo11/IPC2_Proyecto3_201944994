from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Pruebas
def welcome(request):
    return HttpResponse("Bienvenido a Proyecto 3")

def welcomeTemplate(request):
    return render(request, 'welcome.html', {'name': 'Robin Buezo'})