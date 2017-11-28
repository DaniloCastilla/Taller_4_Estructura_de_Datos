
#include <iostream>




#include <conio.h>
/*
*
*         TALLER 4 
*Estructura de Datos- punto 1
*
* @author Danicas99
*	
* @date 25-11-2017
*	
* @version 2
*
*/






using namespace std;


int main()


{


   int vector[5];


   int i, j , temp;






   cout<<" Ingrese los numeros a ordenar "<<endl;


   {


       for(i=0;i<5;i++)


       {


           cout<<i+1<<" -> ";


           cin>>vector[i];


           cout<<endl;


       }


   }



// Exchange method using a temporary



   for(i=0;i<5;i++)


   {


       for(j=i+1;j<5;j++)


       {


           if(vector[j]<vector[i])


           {


               temp=vector[j];


               vector[j]=vector[i];


               vector[i]=vector[j];


               vector[i]=temp;


           }


       }


   }


   for(i=0;i<5;i++)


   {


       cout<<vector[i]<<" ";


   }


   return 0;


}

