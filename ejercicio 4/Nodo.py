class Nodo:
    __clave = None
    __sigIzq = None
    __sigDer = None
    __caracter = None
    def __init__(self,carac,clave):
        self.__caracter = carac
        self.__clave = clave
        self.__sigIzq = None
        self.__sigDer = None

    def setIzquierdo(self, sig):
        self.__sigIzq = sig

    def setDerecho(self, sig):
        self.__sigDer = sig

    def setClave(self, clave):
        self.__clave = clave

    def getClave(self):
        return self.__clave

    def getIzquierdo(self):
        return self.__sigIzq

    def getDerecho(self):
        return self.__sigDer

    def setCaracter(self, caracter):
        self.__caracter = caracter
    def getcaracter(self):
        return self.__caracter

    def __eq__(self, otro):
        if type(otro) == str:
            return self.__caracter == otro

    def __gt__(self, otro):
        if type(otro) == Nodo:
            return otro.getClave() < self.__clave