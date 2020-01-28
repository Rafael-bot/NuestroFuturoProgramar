epackage Herencias;

import Herencias.Clases.*;

public class PersonaMain {

	public static void main(String[] args) {
		Persona p1 = new Persona();
		Adulto a1 = new Adulto();
		Anciano an1 = new Anciano();
		Joven j1 = new Joven();
		System.out.println(p1.toString());
		System.out.println(a1.toString());
		//Persona p2 = new Persona("Manolo");
		//System.out.println(p1.nombre);

	}

}
