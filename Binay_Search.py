'''
Created on 28 nov. 2017

@author: Danicas99
'''
from random import randint
from builtins import str


def Quick_sort(V): #Quick Sort function
    pivote = len(V)//2
    menor, igual, mayor = [],[],[]
    
    for i in range(len(V)):
        if(V[i] < V[pivote]): menor.append(V[i])
        elif(V[i]> V[pivote]): mayor.append(V[i])
        else: igual.append(V[i])
        
    if len(menor)>1: 
        menor = Quick_sort(menor)
    if len(mayor)>1: 
        mayor = Quick_sort(mayor)
    return menor + igual + mayor
    #end funtion
def B_S(V , X): #Binary search Function
    
    Inicio = 0
    Final = (len(V)-1)
    T = False
    
    while(not(T) and Inicio <= Final):
        mitad = int((Inicio + Final)/2)
        if(X == V[mitad]):
            T = True
            Num = mitad
        elif X < V[mitad]:
            Final = mitad - 1
            
        else:
            Inicio = mitad + 1
    print()
    
    if(T):
        return("El Numero se encuentra y se localiza en la posicion " + str(Num))
    else:
        return("El dato no se encuentra")
    print()
    #end Binary Search Funtion
def main(): #Class main
    
    Tamain = (input("Escriba la Sucesion de numeros separados por comas \n"))
    Tamain_2 = Tamain.split(",")
    print()
    Tamain_3 = Tamain.split(",")
    
    for i in range (0,len(Tamain_2)):
        Tamain_3[i] = int(Tamain_2[i])
    print()
    
    Tamain_4 = (Quick_sort(Tamain_3))
    print("El Arreglo ordenado es " + str(Tamain_4))
    
    Valor = int(input("Ingrese un numero a buscar \n"))
    
    Binary = B_S(Tamain_4, Valor)
    print(Binary)
       
       
main()#end class main
