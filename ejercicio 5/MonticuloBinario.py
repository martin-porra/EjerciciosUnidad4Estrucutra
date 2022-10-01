import math
import numpy as np
class Monticulo:
    __arreglo = []
    __tamaño = None

    def __init__(self,tamaño = 10):
        self.__arreglo = np.empty(tamaño,dtype=int)
        self.__tamaño = tamaño
        self.__arreglo[0] = 0
            
    def insertar(self,elemento):
        if not self.lleno():
         actual = self.__arreglo[0]+1
         self.__arreglo[actual] = elemento
         padre = math.floor(actual/2)
         while padre != 0 and self.__arreglo[actual] < self.__arreglo[padre]:
             aux = self.__arreglo[actual]
             self.__arreglo[actual] = self.__arreglo[padre]
             self.__arreglo[padre] = aux
             actual = padre
             padre = math.floor(actual/2)
         self.__arreglo[0]+=1    
        else:
            print('Arreglo Lleno') 
             
    def eliminarMinimo(self):
        if self.vacio():
            print('Arreglo vacio')
        else:
            self.__arreglo[1] = self.__arreglo[self.__arreglo[0]]
            self.__arreglo[0]-=1
            i=1
            while i<self.__arreglo[0]:
                hijoIzquierdo = (i*2)
                hijoDerecho = (i*2)+1
                if hijoIzquierdo <= self.__arreglo[0] and self.__arreglo[hijoIzquierdo] < self.__arreglo[i]:
                    aux = self.__arreglo[i]
                    self.__arreglo[i] = self.__arreglo[hijoIzquierdo]
                    self.__arreglo[hijoIzquierdo] = aux
                if hijoDerecho <= self.__arreglo[0] and self.__arreglo[hijoDerecho] < self.__arreglo[i]:
                    aux = self.__arreglo[i]
                    self.__arreglo[i] = self.__arreglo[hijoDerecho]
                    self.__arreglo[hijoDerecho] = aux           
                i+=1                         
        
    def lleno(self):
        return (self.__arreglo[0]) == self.__tamaño  
    def vacio(self):
        return self.__arreglo[0] == 0  
    def mostrar(self):
        for i in range(1,self.__arreglo[0]+1):
            print(self.__arreglo[i])  
              

if __name__ == '__main__':
    arreglo = Monticulo()    
    arreglo.insertar(1)
    arreglo.insertar(5) 
    arreglo.insertar(4)     
    arreglo.insertar(3) 
    arreglo.insertar(2)
    print('Antes de suprimir') 
    arreglo.mostrar()
    arreglo.eliminarMinimo()
    print('Despues de suprimir') 
    arreglo.mostrar()