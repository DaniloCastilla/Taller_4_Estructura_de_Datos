import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Merge_Sort {
	 public static void imprimeArray(int[] array){
	        for (int i = 0; i < array.length; i++) {
	            System.out.print("[" + array[i] + "]");
	        }
	 }
	 
public static void ordenacionMergeSort(int Array[]){
	if(Array.length<=1) return;
		int mitad= Array.length/2;
		int menor[]=Arrays.copyOfRange(Array, 0, mitad);
		int mayor[]=Arrays.copyOfRange(Array, mitad, Array.length);
			ordenacionMergeSort(menor);
			ordenacionMergeSort(mayor);       
			combinarVector(Array, menor, mayor);
  }
  
  public static void combinarVector(int v[], int izq[],int der[]){
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
  }
  public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader (new InputStreamReader (System.in));	
	BufferedWriter bw = new BufferedWriter (new OutputStreamWriter (System.out));
	
	Merge_Sort M_S = new Merge_Sort() ;
		
	bw.write("escriba el tamaño del arreglo");
	bw.flush();	
	int T = Integer.parseInt(br.readLine());
		
	bw.write("escriba los numeros del arreglo, recuerde que deben ir separados por comas (,) \n");
	bw.flush();
	String Array = br.readLine();
	String [] Array_2 = Array.split(",");
	int Vector [] = new int [T]; 
	
	for (int i = 0; i < Vector.length; i++) {
		Vector [i] = Integer.parseInt(Array_2[i]);
	}
		
	M_S.imprimeArray(Vector);
	System.out.println("\n"+"Merge Sort");
	M_S.ordenacionMergeSort(Vector);
	M_S.imprimeArray(Vector);
	
  }
}
