package Interfaces;

import Interfaces.Clases.*;

public class EjemploMain {

	public static void main(String[] args) {
		
		Perro p = new Perro("Coco");
		Gato g = new Gato("Chispita");
		
		System.out.println(p);
		p.saludar(g);
		p.saludar();
		
		System.out.println();
		System.out.println(g);
		g.saludar(p);
		g.saludar();
		

	}

}
	