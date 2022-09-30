from ClaseArbol import  ArbolBinario
def text():
 print('1 -- Para saber el padre y hermano de un nodo')
 print('2 -- Cantidad de Nodos del arbol')
 print('3 -- Mostrar altura del arbol')
 print('4 -- Mostrar sucesores de un nodo')
 print('0 -- Salir')
if __name__ == '__main__':
 arbol = ArbolBinario()
 arbol.insertar(arbol.getRaiz(), 50)
 arbol.insertar(arbol.getRaiz(), 45)
 arbol.insertar(arbol.getRaiz(), 43)
 arbol.insertar(arbol.getRaiz(), 60)
 arbol.insertar(arbol.getRaiz(), 55)
 arbol.insertar(arbol.getRaiz(), 52)
 arbol.insertar(arbol.getRaiz(), 58)
 arbol.insertar(arbol.getRaiz(), 70)
 band = True
 i = 0
 while band != False:
  text()
  print('ingrese un numero ')
  i = int(input())
  if i == 1:
   nodo = int(input('Ingrese nodo '))
   if type(nodo) == int:
    arbol.Padre_Hermano(nodo)
   else:
    print('No es la clave de un nodo')
  elif i == 2:
   print('Cantidad de nodos del arbol: ', arbol.ContarNodos(arbol.getRaiz()))
  elif i ==3:
   print('La altura del arbol es: ',arbol.getAlturaArbol(arbol.getRaiz()))
  elif i ==4:
   nodo = int(input('Ingrese nodo '))
   if type(nodo) == int:
    print('Los sucesores del nodo')
    arbol.Recorrer(nodo,arbol.getRaiz())
   else:
    print('No es la clave de un nodo')
  elif i == 0:
   print('Cerrar Programa')
   band = False
  else:
   print('opcion incorrecta vuelva a seleccionar')


