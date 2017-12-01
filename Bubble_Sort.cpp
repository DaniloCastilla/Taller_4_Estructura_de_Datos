//============================================================================
// Name        : Bubblesort_c++.cpp
// Author      : Danicas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <conio.h>

 using namespace std;

 void Bubblesort(int array[] , int Tm){ //Method BubbleSort

	 int aux;
	 for(int i = 0 ; i < Tm ; i++){
		 for(int j = 0; j < Tm ; j++){
			 if(array[j] > array[j+1])
			 {
				 aux = array[j];
				 array[j] = array[j+1];
				 array[j+1] = aux;

			 }
		 }
	 }

 }//end Method

  void Imprimir_Arreglo(int array[], int tam){ //method to print array
  	for(int i = 0 ; i < tam ; i++){
 		cout << "["<<array[i]<<"]";
	 }
  }//end method

 int main(){//Main method

	 	int x;
	  	string Cadena;
	    vector<int> vect;

	    cout <<"ingrese el tamaño del arreglo: " << endl;
	    cin >> x;
	    int Vector[x];
	    cout << "Digite la cadena de caracteres separado por comas: \n";
	    cin >> Cadena;
	    stringstream Separated(Cadena);

	    int i;

	    while (Separated >> i){
	         vect.push_back(i);
	         if (Separated.peek() == ',')
	       	Separated.ignore();
	    }

	    int Tm = vect.size();
	    cout << "Tamaño del vector " << Tm << endl;
	    for (i=0; i< Tm; i++){

	     	Vector[i] = vect.at(i);

	    }

	    Bubblesort(Vector,x);

	    cout << "El vector ordenado es" << endl;

	    Imprimir_Arreglo(Vector,x);

	    getch();
	    return 0;


 }//end Method
