from colorama import Fore
from ManagerXml import ManagerXml

class BD:
    def __init__(self, path):
        self.__path = path
        self.__resources = []
        self.__categories = []
        self.__clients = []
        self.__consumeds = []
        self.mngxml = ManagerXml()
        self.__loadBD()

    def __loadBD(self):
        try:
            if self.__path is not None:
                self.__resources, self.__categories, self.__clients, msg = self.mngxml.readConfigsXML(self.__path)
                self.__consumeds, msg = self.mngxml.readConsumedsXML(self.__path)
        except Exception as e:
            print(Fore.RED + f'{e}')

    def __updateBD(self):
        try:
            xml = self.mngxml.createXML(self.__resources, self.__categories, self.__clients, self.__consumeds)
            
            if xml is not None:
                file = open('BD\BD.xml', 'wb')
                file.write(xml)
                file.close()
        except Exception as e:
            print(Fore.RED + f'{e}')
            return [False, e]

    def addConfigs(self, data, path=True):
        try:
            resources, categories, clients, msg = self.mngxml.readConfigsXML(data, path)
            
            msgbd=None
            if msg[0]:
                self.__resources += resources
                self.__categories += categories
                self.__clients += clients
                msgbd = self.__updateBD()
            if msgbd is not None:
                return msgbd
            else:
                return msg
        except Exception as e:
            print(Fore.RED + f'{e}')
            return [False, e]

    def addConsumeds(self, data, path=True):
        try:
            consumeds, msg = self.mngxml.readConsumedsXML(data, path)
            
            msgbd=None
            if msg[0]:
                self.__consumeds += consumeds
                msgbd = self.__updateBD()
            if msgbd is not None:
                return msgbd
            else:
                return msg
        except Exception as e:
            print(Fore.RED + f'{e}')
            return [False, e]

    def getResources(self):
        return self.__resources

    def getCategories(self):
        return self.__categories

    def getClients(self):
        return self.__clients

    def addResource(self, resource):
        self.__resources.append(resource)
        self.__updateBD()
        return 'Recuso creado exitosamente'

    def addCategory(self, category):
        self.__categories.append(category)
        self.__updateBD()
        return 'Categoria creada exitosamente'

    def addConfig(self, idcat, config):
        for cat in self.__categories:
            if cat.getId() == idcat:
                configs = cat.getConfigs()
                configs.append(config)
                cat.setConfigs(configs)
                self.__updateBD()
                return f'Configuración agregada a la categoría {cat.getName()}'
        return 'No se encontró la categoría especificada'
                
    def addClient(self, client):
        self.__clients.append(client)
        self.__updateBD()
        return 'Cliente creado exitosamente'

    def addInstance(self, nitclient, instance):
        for client in self.__clients:
            if client.getNit() == nitclient:
                instances = client.getInstances()
                instances.append(instance)
                client.setInstances(instances)
                self.__updateBD()
                return f'Instancia agregada al cliente {client.getName()}'
        return 'No se encontró al cliente especificado'