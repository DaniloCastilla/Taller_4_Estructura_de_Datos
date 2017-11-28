'''
Created on 28 nov. 2017

@author: Danicas99
'''
from random import randint
from builtins import str


def Quick_sort(V):
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

def B_S(V , X):
    
    Inicio = 0
    Final = (len(V)-1)
    Encontro = False
    
    while(not(Encontro) and Inicio <= Final):
        mitad = int((Inicio + Final)/2)
        if(X == V[mitad]):
            Encontro = True
            Num = mitad
        elif(X < (V[mitad])):
            Final = mitad - 1
            
        else:
            Inicio = mitad + 1
    print()
    
    if(Encontro):
        return("El Numero se encuentra y se localiza en la posicion " + str(Num))
    else:
        return("El dato no se encuentra")
    print()

def main():
    
    Tamain = (input("Escriba la Sucesion de numeros separados por comas \n"))
    print(Tamain)
    Tamain_2 = Tamain.split(",")
    print(Tamain_2)
    Tamain_3 = Quick_sort(Tamain_2)
    print(Tamain_3)
    
    Valor = (input("Ingrese un numero a buscar \n"))
    
    Binary = B_S(Tamain_3, Valor)
    print(Binary)
       
       
main()
