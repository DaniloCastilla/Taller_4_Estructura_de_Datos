//============================================================================
// Name        : LinealSearch_C++.cpp
// Author      : Danicas
// Version     : 1.0
// Copyright   : Your copyright notice
// Description : Ansi-style
//============================================================================

#include <vector>
#include <string>
#include <sstream>
#include <iostream>

 using namespace std;

 int linearSearch(int array[],int tam, int valor){ //Method LinealSearch

	 for(int i = 0 ; i < tam ; i++){
 		if(valor == array [i]){

 			return i;

 		}

	 }
	 return -1;
 }//end Method
  void Imprimir_Arreglo(int array[], int tam){ //method to print array
  	for(int i = 0 ; i < tam ; i++){
 		cout <<" ["<<array[i]<<"] \n";
	 }
  }//end method

 int main (){//Main method

 	int x;
 	int y;

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
    for (i=0; i< Tm; i++){

    	Vector[i] = vect.at(i);
	}

 	cout <<"ingrese numero que desea buscar: " << endl;
 	cin >> y;

	int Index = linearSearch(Vector,x,y);

	Imprimir_Arreglo(Vector,x);

	if(Index>=0){
		cout << "El numero " << Vector[Index]<< " se encontro"
				 " en el indice " << Index << endl;
	}else{
		cout << "El numero " << y <<" no se encontro. "<< endl;
	}

	system("PAUSE");
	return 0;

 }//end method

