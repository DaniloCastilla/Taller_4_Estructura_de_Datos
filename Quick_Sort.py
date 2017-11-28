'''
Created on 28 nov. 2017

@author: Danicas99
'''

from random import randint


def Quick_sort(V): ##Definimos una funcion para el metodo de ordenamiento
    pivote = len(V)//2 ##Seleccionamos un pivote sacando el entero de la divison del arreglo
    menor, igual, mayor = [],[],[] ##Se crean tres matrices para para asignar valores
    
    for i in range(len(V)):
        if(V[i] < V[pivote]): menor.append(V[i])  ##Condicional que pregunta si es igual
            
        elif(V[i]> V[pivote]):  mayor.append(V[i]) ##Segundo condicional que nos dice si es mayo
           
        else: igual.append(V[i]) ##Si no e sigual, ni es mayor, por lo tanto es menor y solo se agrega al arreglo que le correpsonde
        
    if len(menor)>1: 
        menor = Quick_sort(menor)
    if len(mayor)>1: 
        mayor = Quick_sort(mayor)
    return menor + igual + mayor ##Retornará el arreglo ordenado concatenando sus arreglos respectivos


def main():
    
    Tamain = (input("Escriba la Sucesion de numeros separados por comas \n")) ##Escribir los numeros separados por comas
    print(Tamain)
    Tamain_2 = Tamain.split(",") ##Dividir el arreglo
    print(Tamain_2)
    Tamain_3 = (Quick_sort(Tamain_2))
    print(Tamain_3)
    
main()
