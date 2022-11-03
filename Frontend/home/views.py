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

def consultData(requests):
    result = Services.consultData()
    resources = result['data']['listaRecursos']['recurso']
    categories = result['data']['listaCategorias']['categoria']
    clients = result['data']['listaClientes']['cliente']
    return render(requests, 'consultData.html', {'resources': resources, 'categories': categories, 'clients': clients})

def createResource(requests):
    result = ''
    if requests.method == 'POST':
        id = requests.POST.get("id")
        name = requests.POST.get("name")
        abbrev = requests.POST.get("abbrev")
        metrics = requests.POST.get("metrics")
        type = requests.POST.get("type")
        cost = requests.POST.get("cost")

        result = Services.createResource({'id': id, 'name': name, 'abbrev': abbrev, 'metrics': metrics, 'type': type, 'cost': cost})

    return render(requests, 'createResource.html', {'result': result})

def createCategory(requests):
    result = ''
    if requests.method == 'POST':
        id = requests.POST.get("id")
        name = requests.POST.get("name")
        desc = requests.POST.get("desc")
        workload = requests.POST.get("workload")

        result = Services.createCategory({'id': id, 'name': name, 'desc': desc, 'workload': workload})

    return render(requests, 'createCategory.html', {'result': result})

def createConfig(requests):
    result = ''
    if requests.method == 'POST':
        idcat = requests.POST.get("idcat")
        id = requests.POST.get("id")
        name = requests.POST.get("name")
        desc = requests.POST.get("desc")

        result = Services.createConfig({'idcat': idcat, 'id': id, 'name': name, 'desc': desc})

    return render(requests, 'createConfig.html', {'result': result})

def createClient(requests):
    result = ''
    if requests.method == 'POST':
        nit = requests.POST.get("nit")
        name = requests.POST.get("name")
        user = requests.POST.get("user")
        passw = requests.POST.get("passw")
        address = requests.POST.get("address")
        email = requests.POST.get("email")

        result = Services.createClient({'nit': nit, 'name': name, 'user': user, 'passw': passw, 'address': address, 'email': email})

    return render(requests, 'createClient.html', {'result': result})


def createInstance(requests):
    result = ''
    if requests.method == 'POST':
        nitclient = requests.POST.get("nitclient")
        idinstance = requests.POST.get("idinstance")
        idconfig = requests.POST.get("idconfig")
        name = requests.POST.get("name")
        startdate = requests.POST.get("startdate")
        status = requests.POST.get("status")
        enddate = requests.POST.get("enddate")

        result = Services.createInstance({'nitclient': nitclient, 'idinstance': idinstance, 'idconfig': idconfig, 'name': name, 'startdate': startdate, 'status': status, 'enddate': enddate})

    return render(requests, 'createInstance.html', {'result': result})