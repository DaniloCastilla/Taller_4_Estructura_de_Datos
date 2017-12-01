//============================================================================
// Name        : InsertionSort_C++.cpp
// Author      : Danicas
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <vector>
#include <string>
#include <sstream>
#include <iostream>

 using namespace std;

 void InsertionSort(int array[] , int Tm){ //Method InsertionSort

	 int pos;
	 int aux;

	 for (int i = 0; i < Tm; ++i) {

		 pos = i;
		 aux = array[i];

		 while((pos>0)&&(array[pos - 1] > aux)){

			 array[pos] = array[pos-1];
			 pos--;

		 }

		 array[pos] = aux;
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

	    InsertionSort(Vector, Tm); //call method
	    cout << "El vector ordenado es " << endl;

	    Imprimir_Arreglo(Vector,x);//call method to print

	    system("PAUSE");
	    return 0;

 }
