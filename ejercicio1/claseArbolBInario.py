from claseNodo import Nodo

class ArbolBinario:
    __raiz = None
    
    def __init__(self):
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz
    
    def insertar(self,SubArbol,clave):
        if self.__raiz == None:
            nodo = Nodo(clave)
            self.__raiz = nodo
        else:
            if clave > SubArbol.getClave():
                if SubArbol.getSigDerecho() == None:
                    nodo = Nodo(clave)
                    SubArbol.setSigDerecho(nodo)
                else:
                    self.insertar(SubArbol.getSigDerecho(),clave)            
            elif clave < SubArbol.getClave():
                if SubArbol.getSigIzquierdo() == None:
                    nodo = Nodo(clave)
                    SubArbol.setSigIzquierdo(nodo)
                else:
                    self.insertar(SubArbol.getSigIzquierdo(),clave)
            else:
                print('ERROR: Elemento ya existente!')
    
    def InOrder(self,SubArbol):
        if not SubArbol == None:
            self.InOrder(SubArbol.getSigIzquierdo())
            if self.gradoNodo(SubArbol.getClave()) == 0:
             print(SubArbol.getClave())
            self.InOrder(SubArbol.getSigDerecho())

    def preOrder(self,SubArbol):
        if not SubArbol == None:
            print(SubArbol.getClave())
            self.preOrder(SubArbol.getSigIzquierdo())
            self.preOrder(SubArbol.getSigDerecho())
    
    def buscar(self, SubArbol, clave):
        if SubArbol != None:
            if clave == SubArbol.getClave():
                return SubArbol
            elif clave > SubArbol.getClave():
                nodo = self.buscar(SubArbol.getSigDerecho(),clave)
            else:
                nodo = self.buscar(SubArbol.getSigIzquierdo(), clave)
        else:
            print('Elmento no encontrado!')
        return nodo
    
    def getInfimo(self, raiz):
        subarbol = raiz
        if raiz.getSigDerecho() != None:
            subarbol = raiz.getSigDerecho()
            self.getInfimo(raiz.getSigDerecho())
        return subarbol
    
    def Padre(self, subArbol,  elemento, ant=None):
        if subArbol != None:
            if subArbol.getClave() == elemento:
               if ant == None:
                   print('No tiene padre es raiz')
               else:
                    return ant

            elif subArbol.getClave() > elemento:
              return self.Padre(subArbol.getSigIzquierdo(), elemento, subArbol)
            else:
               return self.Padre(subArbol.getSigDerecho(), elemento, subArbol)
        else:
            print('ERROR: Elemento no encontrado!')
        return ant
    def nivel(self,valor):
        nivel = 0
        nodo = self.__raiz
        while nodo != None:
          if nodo.getClave() == valor:
              nodo = None
          elif nodo.getClave() > valor:
              nodo = nodo.getSigIzquierdo()
          else:
              nodo = nodo.getSigDerecho()
          nivel+=1
        return nivel
    def hijo(self,x,y):
        padre = self.buscar(self.__raiz,x)
        band = False
        if padre.getSigIzquierdo().getClave() == y or  padre.getSigDerecho().getClave() == y:
            band = True
        return  band
    def hoja(self,x):
        aux = self.buscar(self.__raiz,x)
        band = False
        if aux.getSigIzquierdo() == None and aux.getSigDerecho() == None:
            band = True
        return band

    def getAlturaArbol(self, subArbol, max=1):
        if subArbol != None:
            nivel = self.nivel(subArbol.getClave())
            if max < nivel:
                max = nivel
            max = self.getAlturaArbol(subArbol.getSigIzquierdo(), max)
            max = self.getAlturaArbol(subArbol.getSigDerecho(), max)
        return max
    def gradoNodo(self,clave):
        nodo =  self.buscar(self.__raiz,clave)
        if nodo != None:
            if nodo.getSigIzquierdo() != None and nodo.getSigDerecho() != None:
                grado = 2
            elif (nodo.getSigIzquierdo() != None and nodo.getSigDerecho() == None) or (nodo.getSigIzquierdo() == None and nodo.getSigDerecho() != None):
                grado =1
            else:
                grado = 0
        return  grado


    def suprimir(self, subArbol , clave):
        nodo = self.buscar(subArbol,clave)
        padre = self.Padre(subArbol, clave, None)
        if nodo != None:
                if nodo.getSigIzquierdo() == None and nodo.getSigDerecho() == None:#Caso 1: El nodo es de grado 0
                    if padre == None:
                        self.__raiz = None
                    else:
                        if padre.getClave() > clave:
                            padre.setSigIzquierdo(None)
                        else:
                            padre.setSigDerecho(None)
                elif nodo.getSigIzquierdo() != None and nodo.getSigDerecho() == None: #Caso 2: el nodo es de grado 1 
                    if padre == None:
                        if self.__raiz.getClave() > clave:
                            self.__raiz = self.__raiz.getSigDerecho()
                        else:
                      
                            self.__raiz = self.__raiz.getSigIzquierdo()
                    else:
                        if padre.getClave() > clave:
                            padre.setSigIzquierdo(nodo.getSigIzquierdo())
                        else:
                            padre.setSigDerecho(nodo.getSigIzquierdo())
                   
                elif nodo.getSigIzquierdo() == None and nodo.getSigDerecho() != None:
                    if padre == None:
                        if self.__raiz.getClave() > clave:
                              self.__raiz = self.__raiz.getSigIzquierdo()
                        else:
                            self.__raiz = self.__raiz.getSigDerecho()
                    else:
                        if padre.getClave() > clave:
                            padre.setSigIzquierdo(nodo.getSigDerecho())
                        else:
                            padre.setSigDerecho(nodo.getSigDerecho())
                    
                else:#Caso 3: el nodo es de grado 2
                    maximo = self.getInfimo(nodo.getSigIzquierdo())
                    nuevaClave = maximo.getClave()
                    self.suprimir(self.__raiz, nuevaClave)
                    nodo.setClave(nuevaClave)


        
if __name__ == '__main__':
    objArbol = ArbolBinario()
    objArbol.insertar(objArbol.getRaiz(),50)
    objArbol.insertar(objArbol.getRaiz(), 45)
    objArbol.insertar(objArbol.getRaiz(),60)
    objArbol.insertar(objArbol.getRaiz(),55)
    objArbol.insertar(objArbol.getRaiz(),52)
    objArbol.insertar(objArbol.getRaiz(),58)
    objArbol.insertar(objArbol.getRaiz(),70)
    print('Antes de suprimir')
    objArbol.preOrder(objArbol.getRaiz())
    #objArbol.suprimir(objArbol.getRaiz(),60 )
    #print('Despues de suprimir')
    #objArbol.preOrder(objArbol.getRaiz())
    #print(objArbol.Padre(objArbol.getRaiz(),45).getClave())
    #print(objArbol.nivel(52))
    #print(objArbol.getAlturaArbol(objArbol.getRaiz()))
    print('frontera')
    objArbol.InOrder(objArbol.getRaiz())