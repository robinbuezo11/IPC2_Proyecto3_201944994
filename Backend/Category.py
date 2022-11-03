
class Category:
    def __init__(self, id, name, description, workloaddef, configs=[]):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__workloaddef = workloaddef
        self.__configs = configs

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__description

    def getWorkLoad(self):
        return self.__workloaddef

    def getConfigs(self):
        return self.__configs

    def setConfigs(self, configs):
        self.__configs = configs