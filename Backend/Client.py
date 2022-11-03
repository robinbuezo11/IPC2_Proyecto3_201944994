
class Client:
    def __init__(self, nit, name, user, passw, address, email, instances=[]):
        self.__nit = nit
        self.__name = name
        self.__user = user
        self.__passw = passw
        self.__address = address
        self.__email = email
        self.__instances = instances

    def getNit(self):
        return self.__nit

    def getName(self):
        return self.__name

    def getUser(self):
        return self.__user

    def getPassw(self):
        return self.__passw

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def getInstances(self):
        return self.__instances

    def setInstances(self, instances):
        self.__instances = instances