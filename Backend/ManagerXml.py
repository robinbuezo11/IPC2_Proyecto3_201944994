from colorama import Fore
import xml.etree.ElementTree as et
import re
from Category import Category
from Client import Client
from Config import Config
from Instance import Instance
from Resource import Resource

class ManagerXml():
    def __init__(self):
        pass

    def readConfigsFile(self, path):
        try:
            self.__tree = et.parse(path)
            self.__root = self.__tree.getroot()
            for iter in self.__root:
                if iter.tag == 'listaRecursos':
                    resources = []
                    for resource in iter:
                        idresource = resource.attrib['id']
                        for iresource in resource:
                            if iresource.tag == 'nombre':
                                nameresource = iresource.text
                            elif iresource.tag == 'abreviatura':
                                abbreviationresource = iresource.text
                            elif iresource.tag == 'metrica':
                                metricsresource = iresource.text
                            elif iresource.tag == 'tipo':
                                if iresource.text in ['Hardware','Software']:
                                    typeresource = iresource.text
                                else:
                                    return
                            elif iresource.tag == 'valorXhora':
                                costresource = float(iresource.text)
                        newresource = Resource(idresource, nameresource, abbreviationresource, metricsresource, typeresource, costresource)
                        resources.append(newresource)
                elif iter.tag == 'listaCategorias':
                    categories = []
                    for category in iter:
                        idcategory = category.attrib['id']
                        for icategory in category:
                            if icategory.tag == 'nombre':
                                namecategory = icategory.text
                            elif icategory.tag == 'descripcion':
                                descriptioncategory = icategory.text
                            elif icategory.tag == 'cargaTrabajo':
                                workloaddefcategory = icategory.text
                            elif icategory.tag == 'listaConfiguraciones':
                                configs = []
                                for config in icategory:
                                    idconfig = config.attrib['id']
                                    for iconfig in config:
                                        if iconfig.tag == 'nombre':
                                            nameconfig = iconfig.text
                                        elif iconfig.tag == 'descripcion':
                                            descriptionconfig = iconfig.text
                                        elif iconfig.tag == 'recursosConfiguracion':
                                            resourcesconfig = []
                                            for resource in iconfig:
                                                resourcesconfig.append([resource.attrib['id'],resource.text])
                                    newconfig = Config(idconfig, nameconfig, descriptionconfig, resourcesconfig)
                                    configs.append(newconfig)
                        newcategory = Category(idcategory, namecategory, descriptioncategory, workloaddefcategory, configs)
                        categories.append(newcategory)
                elif iter.tag == 'listaClientes':
                    clients = []
                    for client in iter:
                        nitclient = client.attrib['nit']
                        for iclient in client:
                            if iclient.tag == 'nombre':
                                nameclient = iclient.text
                            elif iclient.tag == 'usuario':
                                userclient = iclient.text
                            elif iclient.tag == 'clave':
                                passwclient = iclient.text
                            elif iclient.tag == 'direccion':
                                addressclient = iclient.text
                            elif iclient.tag == 'correoElectronico':
                                emailclient = iclient.text
                            elif iclient.tag == 'listaInstancias':
                                instances = []
                                for instance in iclient:
                                    idinstance = instance.attrib['id']
                                    for iinstance in instance:
                                        if iinstance.tag == 'idConfiguracion':
                                            idconfiginst = iinstance.text
                                        elif iinstance.tag == 'nombre':
                                            nameinstance = iinstance.text
                                        elif iinstance.tag == 'fechaInicio':
                                            startdate = iinstance.text
                                        elif iinstance.tag == 'estado':
                                            active = iinstance.text
                                        elif iinstance.tag == 'fechaFinal':
                                            enddate = iinstance.text
                                    newinstance = Instance(idinstance, idconfiginst, nameinstance, startdate, active, enddate)
                                    instances.append(newinstance)
                        newclient = Client(nitclient, nameclient, userclient, passwclient, addressclient, emailclient, instances)
                        clients.append(newclient)
            return resources, categories, clients
        except Exception as e:
            print(Fore.RED + f'{e}')
            pass

    def readConsumedsFile(self, path):
        try:
            self.__tree = et.parse(path)
            self.__root = self.__tree.getroot()
            consumeds = []
            for consumed in self.__root:
                nitclient = consumed.attrib['nitCliente']
                idinstance = consumed.attrib['idInstancia']
                for iconsumed in consumed:
                    if iconsumed.tag == 'tiempo':
                        time = iconsumed.text
                    elif iconsumed.tag == 'fechaHora':
                        datetime = iconsumed.text
                newconsumed = [nitclient, idinstance, time, datetime]
                consumeds.append(newconsumed)
            return consumeds
        except Exception as e:
            print(Fore.RED + f'{e}')
            pass