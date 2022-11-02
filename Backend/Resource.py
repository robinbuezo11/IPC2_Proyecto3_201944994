
class Resource:
    def __init__(self, id, name, abbreviation, metrics, type, cost, quantity=0):
        self.__id = id
        self.__name = name
        self.__abbreviation = abbreviation
        self.__metrics = metrics
        self.__type = type
        self.__cost = cost
        self.__quantity = quantity

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getAbbreviation(self):
        return self.__abbreviation

    def getMetrics(self):
        return self.__metrics
    
    def getType(self):
        return self.__type

    def getCost(self):
        return self.__cost
    