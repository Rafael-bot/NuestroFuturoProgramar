package Introducción.Ejercicio;

import Introducción.Ejercicio.Clase.clasesContacto;
import Introducción.Ejercicio.Clase.clasesAgenda;
import java.util.Scanner;

public class Movil {

	public static void main(String[] args) {
		clasesAgenda agenda = new clasesAgenda();
		clasesContacto c1 = new clasesContacto("Lolo");
		clasesContacto c2 = new clasesContacto("Pepa", 123456789);
		clasesContacto c3 = new clasesContacto("Joselito", "123456789");
		c1.setNombre("Paco");
		String nombre = c1.getNombre();
		System.out.println(nombre);
		
		clasesContacto[] contactos = new clasesContacto[3];
		contactos[0] = c1;
		contactos[1] = c2;
		contactos[2] = c3;
		

		agenda.contactos = contactos;

		System.out.println(agenda.contactos[2].getNombre());
		
		
	}

}


