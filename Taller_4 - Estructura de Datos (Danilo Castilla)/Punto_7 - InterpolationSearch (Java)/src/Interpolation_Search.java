/**
 * @author Danicas99
 * @date 28/11/2017
 * @version 1.0
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Interpolation_Search {//Main Class
	 public static void imprimeArray(int[] array){
	        for (int i = 0; i < array.length; i++) {
	            System.out.print("[" + array[i] + "]");
	        }
	 }
	 public static void ordenacionMergeSort(int Array[])
	 {//Method that assigns new arrays to divide
	if(Array.length<=1) return;
		int mitad= Array.length/2;
		int menor[]=Arrays.copyOfRange(Array, 0, mitad);
		int mayor[]=Arrays.copyOfRange(Array, mitad, Array.length);
			ordenacionMergeSort(menor);
			ordenacionMergeSort(mayor);       
			combinarVector(Array, menor, mayor);
	 }//end method

	 public static void combinarVector(int v[], int izq[],int der[])
	 {//Method that starts to make combinations of left and right
       int i=0;
       int j=0;
       for(int k=0;k<v.length;k++){
               if(i>=izq.length){
                       v[k]=der[j];
                       j++;
                       continue;
               }
               if(j>=der.length){
                       v[k]=izq[i];
                       i++;
                       continue;
               }
               if(izq[i]<der[j]){
                       v[k]=izq[i];
                       i++;
               }else{
                       v[k]=der[j];
                       j++;
               }
       }
	 }//end method
	
 static int BusquedaInterpolacion(int x, int []arr) 
 {//Method that verifies and searches for the value entered
	 
	 int lowerBound = 0;
	 int higherBound = (arr.length - 1);
	 while (lowerBound <= higherBound && x >= arr[lowerBound] && x <= arr[higherBound]){
		 int middle = lowerBound + (((higherBound-lowerBound) /(arr[higherBound]-arr[lowerBound]))*(x - arr[lowerBound]));
		 if (arr[middle] == x)
	      return middle;
		 
		 if (arr[middle] < x)
			 lowerBound = middle + 1;
	      else
	    	  
	    	  higherBound = middle - 1;
	        }
	        return -1;
	    }//end method

 public static void main(String[] args) throws IOException {//Main method
	BufferedReader br = new BufferedReader (new InputStreamReader (System.in));	
	BufferedWriter bw = new BufferedWriter (new OutputStreamWriter (System.out));		
	
	Interpolation_Search I_S= new Interpolation_Search() ;
				
	bw.write("escriba el tamaño del arreglo");
	bw.flush();	
	int T = Integer.parseInt(br.readLine());
				
	bw.write("escriba los numeros del arreglo, recuerde que deben ir separados por comas (,) \n");
	bw.flush();
	String Arreglo= br.readLine();
	
	String [] Particion = Arreglo.split(",");
	int array [] = new int [T]; 
	for (int i = 0; i < array.length; i++) {
		  array[i]=Integer.parseInt(Particion[i]);
		  System.out.print("["+array[i]+"]");
		}
	
	System.out.println("\n"+"Merge Sort");
	ordenacionMergeSort(array);
	imprimeArray(array);
	
	bw.write("\nEscriba el numero que desea buscar");
	bw.flush();	
	int buscar = Integer.parseInt(br.readLine());
			
	int index= BusquedaInterpolacion(buscar, array);			
	
	System.out.print("\n"+"Busqueda por Interpolación \n");
	
	if (index != -1) 
		System.out.println("es numero se encuentra en la posición o indice numero: "+index);
	
	else
	System.out.println("el numero no se encuentra dentro del arreglo");
    	
	  }//end Method
}//end Class