package Introducci�n.Ejercicio;

import Introducci�n.Ejercicio.Clase.clasesContacto;
import java.util.Scanner;

public class Movil {

	public static void main(String[] args) {
		clasesContacto interior = new clasesContacto();
		Scanner sc = new Scanner(System.in);
		
		boolean control = true;		
		
		while(control){
			System.out.println("----------------------------------");
		clasesContacto.recorridocontact();
		System.out.println("----------------------------------");
		System.out.println("|  1.Seleccionar contacto        |");
		System.out.println("|  2.A�adir contacto             |");
		System.out.println("----------------------------------");
		System.out.print("\t\t");int menu = sc.nextInt();
		System.out.println();
		switch (menu) {
		
		case 1:
			
			break;
		
		case 2:
			
			break;

		default:
			System.out.println("\t !!!ERROR!!!");
			break;
		}	
		}
		
		
		
		
	}

}
