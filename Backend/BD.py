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
                file = open('Backend\BD\BD.xml', 'wb')
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