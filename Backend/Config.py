
class Config:
    def __init__(self, id, name, description, resources=[]):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__resources = resources

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__description
    
    def getResources(self):
        return self.__resources