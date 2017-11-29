'''
Created on 28 nov. 2017

@author: Danicas99
'''

from random import randint #import Library
from builtins import int


def Quick_sort(V): #Quick Sort function, Sort numbers upward
    pivote = int(len(V)/2) 
    menor, igual, mayor = [],[],[] 
    
    for i in range(len(V)):
        if V[i] < V[pivote]: menor.append(V[i])
            
        elif V[i] > V[pivote]:  mayor.append(V[i])
           
        else: igual.append(V[i])
    print()
    
    if len(menor)>1: menor = Quick_sort(menor)
    if len(mayor)>1: mayor = Quick_sort(mayor)
    return menor + igual + mayor #end funtion


def main(): #main funtion
    
    Tamain = (input("Escriba la Sucesion de numeros separados por comas \n"))
    print(Tamain)
    Tamain_2 = Tamain.split(",")
    print(Tamain_2)
    Tamain_3 = Tamain.split(",")
    
    for i in range (0,len(Tamain_2)):
        Tamain_3[i] = int(Tamain_2[i])
    print(Tamain_3)
    
    print(Quick_sort(Tamain_3))
    
main()#end class funtion
