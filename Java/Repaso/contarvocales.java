package Repaso;

import java.util.Scanner;

public class contarvocales {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("\t Introduce la Palabra: "); String palabra = sc.nextLine();
		System.out.print("\t Selecciona el caracter: "); char caracter = sc.next().charAt(0);	
		
		char letras;
		int numletras = palabra.length();
		int vocales = 0;
		int caracteres = 0;
		
		for (int cont = 0; cont < numletras; cont++) {
			letras = palabra.charAt(cont);
			if (letras == caracter) {
				vocales++;
			}
			caracteres++;
		}
		
		System.out.println("------------------------------------------------------");
		System.out.println("\t Hay "+vocales+" de Caracter.");
		System.out.println("\t Hay "+caracteres+" de Caracteres.");
		System.out.print("------------------------------------------------------");
		
		
	}

}
