package Herencias;

import Herencias.Clases.*;

public class Productomain {
	
	public static void main(String[] args) {
		Producto [] productos = new Producto[3];
	
		productos[0] = new Producto("producto 1", 10);
		productos[1] = new Caducado("Producto 2", 20, 1);
		productos[2] = new NoCaducado("Producto 3", 5, "Tipo 1");
	
				
		double total = 0;
		
		for (int cont = 0; cont < productos.length; cont++) {
			total += productos[cont].calcular(5); 
		}
		
		System.out.println("El total es "+total);
	}
}
