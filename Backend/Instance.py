
class Instance:
    def __init__(self, id, idconfig, name, startdate, status, enddate):
        self.__id = id
        self.__idconfig = idconfig
        self.__name = name
        self.__startdate = startdate
        self.__status = status
        self.__enddate = enddate

    def getId(self):
        return self.__id

    def getIdConfig(self):
        return self.__idconfig

    def getName(self):
        return self.__name
    
    def getStartDate(self):
        return self.__startdate

    def getStatus(self):
        return self.__status

    def getEndDate(self):
        return self.__enddate