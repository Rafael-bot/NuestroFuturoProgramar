package Repaso;

import java.util.Arrays;
import java.util.Scanner;

public class Arraynumeroscerca {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int [] num = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
		
		
		System.out.println("-----------------------------------------------------------------------");
		System.out.println(Arrays.toString(num));
		System.out.println("-----------------------------------------------------------------------");
		System.out.println();
		System.out.print("\t Introduce el numero: "); int numero = sc.nextInt();
		
		System.out.println();
		System.out.println();
		
		
		if (numero > num[19]) {
			System.out.println("\t FUERA DE RANGO");
			
		}else {
				System.out.println("------------------------------------------------------------------------");
			
			for (int cont = 0; cont <= 9; cont++) {
					
					if (num[cont] == numero) {
						System.out.print(num[cont]+" ");
					}		
		
			}
			
			boolean control = true;
			
			for (int cont = 10; control == true; cont++) {				
					if (numero == 0) {
						System.out.print("10 ");
						System.out.print("20");
						control = false;
					} 
					if (numero == 1) {
						System.out.print("11");
						control = false;
					} 
					if (numero == 2) {
						System.out.print("12");
						control = false;
					}
					if (numero == 3) {
						System.out.print("13");
						control = false;
					} 
					if (numero == 4) {
						System.out.print("14");
						control = false;
					} 
					if (numero == 5) {
						System.out.print("15");
						control = false;
					} 
					if (numero == 6) {
						System.out.print("16");
						control = false;
					} 
					if (numero == 7) {
						System.out.print("17");
						control = false;
					} 
					if (numero == 8) {
						System.out.print("18");
						control = false;
					} 
					if (numero == 9) {
						System.out.print("19");
						control = false;
					}
			 
			}
			System.out.println();
			System.out.println("------------------------------------------------------------------------");
		}
	}

}
/*
 *Introducimos un numero y nos da el o los numeros que estan en la array que termine por ese numero introducido 
 */
