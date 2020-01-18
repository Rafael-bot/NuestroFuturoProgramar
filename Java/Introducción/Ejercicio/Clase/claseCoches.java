package Introducción.Ejercicio.Clase;

public class claseCoches {//Marca, Modelo, y color
	public static String[] modelo;
	public static String[] color;
	public static String[] marca;
	
	public static void coches() {
		for (int cont = 0; cont < 5; cont++) {
			System.out.println(modelo[cont]);
			System.out.println(marca[cont]);
			System.out.println(color[cont]);
		}
	}
}
