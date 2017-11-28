'''
Created on 28 nov. 2017

@author: Danicas99
'''

from random import randint

def Quick_sort(V): #funtion quick sort, parameter: Array
    pivote = len(V)//2 #Mark pivote (index)
    menor, igual, mayor = [],[],[] #create three array
    
    for i in range(len(V)):#cycle for since 0 to tamain of the array
        if(V[i] < V[pivote]): menor.append(V[i]) #conditional (if array v in the possition i is less to array v in the possition pivote, add to menor this value
        elif(V[i]> V[pivote]): mayor.append(V[i])#conditional (if array v in the possition i is gigher to array v in the possition pivote, add to menor this value
        else: igual.append(V[i])#end conditional #conditional (if array v in the possition i is gigher to array v in the possition pivote, add to menor this value
        
    if len(menor)>1: #if the size is higher to 1, join the funtion and will arrange 
        menor = Quick_sort(menor)#order less
    if len(mayor)>1: #if the size is higher to 1, join the funtion and will arrange 
        mayor = Quick_sort(mayor) #order higher
    return menor + igual + mayor #return the three arrays in order

def main():
    
    Tamain = (input("Escriba la Sucesion de numeros separados por comas \n")) ##Escribir los numeros separados por comas
    print(Tamain)
    Tamain_2 = Tamain.split(",") ##Dividir el arreglo
    print(Tamain_2)
    Tamain_3 = (Quick_sort(Tamain_2))
    print(Tamain_3)
    
main()
