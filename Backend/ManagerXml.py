from colorama import Fore
import xml.etree.ElementTree as et
from Category import Category
from Client import Client
from Config import Config
from Instance import Instance
from Resource import Resource

class ManagerXml():
    def __init__(self):
        pass

    def readConfigsXML(self, data, path=True):
        try:
            if path:
                root = et.parse(data).getroot()
            else:
                root = et.fromstring(data)
            resources = [] 
            categories =[]
            clients = []
            for iter in root:
                if iter.tag == 'listaRecursos':
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
                                if iresource.text.replace(' ','') in ['Hardware','Software']:
                                    typeresource = iresource.text
                                else:
                                    return [],[],[],[False,'El tipo de recurso es incorrecto, debe ser \'Hardware\' o \'Software\'']
                            elif iresource.tag == 'valorXhora':
                                costresource = float(iresource.text)
                        newresource = Resource(idresource, nameresource, abbreviationresource, metricsresource, typeresource, costresource)
                        resources.append(newresource)
                elif iter.tag == 'listaCategorias':
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
                                            status = iinstance.text
                                        elif iinstance.tag == 'fechaFinal':
                                            enddate = iinstance.text
                                    newinstance = Instance(idinstance, idconfiginst, nameinstance, startdate, status, enddate)
                                    instances.append(newinstance)
                        newclient = Client(nitclient, nameclient, userclient, passwclient, addressclient, emailclient, instances)
                        clients.append(newclient)
            return resources, categories, clients, [True,'Información procesada exitosamente']
        except Exception as e:
            print(Fore.RED + f'{e}')
            return [],[],[],[False, e]

    def readConsumedsXML(self, data, path=True):
        try:
            if path:
                root = et.parse(data).getroot()
            else:
                root = et.fromstring(data)
            consumeds = []
            if root.tag == 'listadoConsumos':
                for consumed in root:
                    nitclient = consumed.attrib['nitCliente']
                    idinstance = consumed.attrib['idInstancia']
                    for iconsumed in consumed:
                        if iconsumed.tag == 'tiempo':
                            time = iconsumed.text
                        elif iconsumed.tag == 'fechaHora':
                            datetime = iconsumed.text
                    newconsumed = [nitclient, idinstance, time, datetime]
                    consumeds.append(newconsumed)
            return consumeds, [True,'Información procesada exitosamente']
        except Exception as e:
            print(Fore.RED + f'{e}')
            return [],[False, e]

    def createXML(self, resources, categories, clients, consumeds):
        try:
            data = et.Element('data')

            addresources = et.SubElement(data, 'listaRecursos')
            for resource in resources:
                addresource = et.SubElement(addresources, 'recurso', {'id': resource.getId()})
                addnamres = et.SubElement(addresource, 'nombre')
                addnamres.text = resource.getName()
                addabbrevres = et.SubElement(addresource, 'abreviatura')
                addabbrevres.text = resource.getAbbreviation()
                addmetres = et.SubElement(addresource, 'metrica')
                addmetres.text = resource.getMetrics()
                addtypres = et.SubElement(addresource, 'tipo')
                addtypres.text = resource.getType()
                addcosres = et.SubElement(addresource, 'valorXhora')
                addcosres.text = str(resource.getCost())

            addcategories = et.SubElement(data, 'listaCategorias')
            for category in categories:
                addcategory = et.SubElement(addcategories, 'categoria', {'id': category.getId()})
                addnamcat = et.SubElement(addcategory, 'nombre')
                addnamcat.text = category.getName()
                adddescat = et.SubElement(addcategory, 'descripcion')
                adddescat.text = category.getDesc()
                addworkcat = et.SubElement(addcategory, 'cargaTrabajo')
                addworkcat.text = category.getWorkLoad()
            
                addconfigs = et.SubElement(addcategory, 'listaConfiguraciones')
                for config in category.getConfigs():
                    addconfig = et.SubElement(addconfigs, 'configuracion', {'id': config.getId()})
                    addnamconf = et.SubElement(addconfig, 'nombre')
                    addnamconf.text = config.getName()
                    adddesconf = et.SubElement(addconfig, 'descripcion')
                    adddesconf.text = config.getDesc()

                    addresourcesconf = et.SubElement(addconfig, 'recursosConfiguracion')
                    for res in config.getResources():
                        addresconf = et.SubElement(addresourcesconf, 'recurso', {'id':res[0]})
                        addresconf.text = res[1]
        
            addclients = et.SubElement(data, 'listaClientes')
            for client in clients:
                addclient = et.SubElement(addclients, 'cliente', {'nit': client.getNit()})
                addnamcli = et.SubElement(addclient, 'nombre')
                addnamcli.text = client.getName()
                addusercli = et.SubElement(addclient, 'usuario')
                addusercli.text = client.getUser()
                addpasscli = et.SubElement(addclient, 'clave')
                addpasscli.text = client.getPassw()
                addaddrecli = et.SubElement(addclient, 'direccion')
                addaddrecli.text = client.getAddress()
                addemaicli = et.SubElement(addclient, 'correoElectronico')
                addemaicli.text = client.getEmail()

                addinstances = et.SubElement(addclient, 'listaInstancias')
                for instance in client.getInstances():
                    addinstance = et.SubElement(addinstances, 'instancia', {'id': instance.getId()})
                    addidconf = et.SubElement(addinstance, 'idConfiguracion')
                    addidconf.text = instance.getIdConfig()
                    addnaminst = et.SubElement(addinstance, 'nombre')
                    addnaminst.text = instance.getName()
                    addstardat = et.SubElement(addinstance, 'fechaInicio')
                    addstardat.text = instance.getStartDate()
                    addstatinst = et.SubElement(addinstance, 'estado')
                    if instance.getStatus() == 'Cancelada':
                        addstatinst.text = instance.getStatus()
                    else: 
                        addstatinst.text = 'Vigente'
                    addenddat = et.SubElement(addinstance, 'fechaFinal')
                    addenddat.text = instance.getEndDate()

            addconsumeds = et.SubElement(data, 'listadoConsumos')
            for consumed in consumeds:
                addconsumed = et.SubElement(addconsumeds, 'consumo', {'nitCliente': consumed[0],'idInstancia': consumed[1]})
                addtimcons = et.SubElement(addconsumed, 'tiempo')
                addtimcons.text = consumed[2]
                adddatcons = et.SubElement(addconsumed, 'fechaHora')
                adddatcons.text = consumed[3]
            
            return et.tostring(data)
        except Exception as e:
            print(Fore.RED + f'{e}')
            return None