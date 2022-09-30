import string
from Nodo import Nodo
class Arbol:
    __raiz = None

    def __init__(self):
        self.__raiz = None
        lista = []
        archivo = open('Text.txt')
        text = ''
        for linea in archivo:
            text+= linea
        text = text.translate({ord(c): None for c in string.whitespace}).lower()
        for i in range(len(text)):
            if text[i] not in lista:
                nodo = Nodo(text[i], text.count(text[i]))
                lista.append(nodo)
        lista.sort()
        while len(lista) >= 2:
            NuevoNodo = Nodo(lista[0].getcaracter() + lista[1].getcaracter(),
                                  lista[0].getClave() + lista[1].getClave())

            NuevoNodo.setIzquierdo(lista[0])
            NuevoNodo.setDerecho(lista[1])
            lista.pop(0)
            lista.pop(0)
            lista.append(NuevoNodo)
            lista.sort()

        self.__raiz = lista[0]

    def PreOrden(self, SubArbol):
        if SubArbol != None:
            print("Caracter/es: {}, Frecuencia: {}".format(SubArbol.getcaracter(), SubArbol.getClave()))
            self.PreOrden(SubArbol.getIzquierdo())
            self.PreOrden(SubArbol.getDerecho())

    def Caracter(self, SubArbol):
        if SubArbol != None:
            if SubArbol.getIzquierdo() == None and SubArbol.getDerecho() == None:
              print("Caracter: {}, Frecuencia: {}".format(SubArbol.getcaracter(), SubArbol.getClave()))
            self.Caracter(SubArbol.getIzquierdo())
            self.Caracter(SubArbol.getDerecho())
    def getRaiz(self):
        return self.__raiz
