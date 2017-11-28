'''
Created on 28 nov. 2017

@author: Danicas99
'''
from random import randint #import library random
from builtins import str #import library String


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

def B_S(V , X):#funtion binary search, parameter: Array and Value to search
    
    Inicio = 0 #begin the possition 0
    Final = (len(V)-1) #end the final possition
    Encontro = False #discriminator
    
    while(not(Encontro) and Inicio <= Final):#while the discriminator is False, do
        mitad = int((Inicio + Final)/2) #assignate a valuer integer to mitad
        if(X == V[mitad]): #conditional where he asks if it's equal to mitad
            Encontro = True #if is true, encontro will be true and end the cycle
            Num = mitad #save the index
        elif(X < (V[mitad])): #conditional where he asks if it's less to mitad
            Final = mitad - 1
            
        else:#conditional where he asks if it's higher to mitad
            Inicio = mitad + 1
    print()
    
    if(Encontro):#if encontro is true; will return a messagge with its index
        return("El Numero se encuentra y se localiza en la posicion " + str(Num))
    else:#if encontro is false; will return a messagge with its index
        return("El dato no se encuentra")
    print()

def main():
    
    Tamain = (input("Escriba la Sucesion de numeros separados por comas \n"))#write number separte with commas
    print(Tamain)#to print
    Tamain_2 = Tamain.split(",")
    print(Tamain_2)#divide in arrays
    Tamain_3 = Quick_sort(Tamain_2)#order the new array
    print(Tamain_3)#to print array
    
    Valor = (input("Ingrese un numero a buscar \n"))#value to search
    
    Binary = B_S(Tamain_3, Valor)#call funtion search
    print(Binary)#to print messagge and index
       
       
main()
