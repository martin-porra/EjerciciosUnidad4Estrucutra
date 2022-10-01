import random
from MonticuloBinario import Monticulo
if __name__ == '__main__':
    arreglo = Monticulo(30)
    tiempoatencion = 4
    tiempollegada = 2
    contadoratencion=0
    i =0
    cantidadatendidos= 0
    while i < 30:
         if 1/tiempollegada == (random.randint(0,1)/tiempollegada):
            print('Llego un paciente')
            arreglo.insertar(random.randint(1,20))
         if contadoratencion == 4:
                if not arreglo.vacio():
                    print('Se atendio un paciente')
                    cantidadatendidos+=1 
                    arreglo.eliminarMinimo()
                    contadoratencion = 0
         contadoratencion+=1        
         i+=1
    print('Cantidad de pacientes atendidos {}'.format(cantidadatendidos))    

     