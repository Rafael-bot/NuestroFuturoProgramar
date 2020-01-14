package Introducción.Ejercicio.Clase;

public class clasePersona {
	
	//Variable
	public static String nombre;
	public static int edad;
	public static float altura;
	public static String dni;
	
	public static boolean mayoredad() {
		if (edad >= 18) {
			return true;
		}
		return false;		
	}
	
	public static boolean rangodni() {
		if (dni.length() <= 9) {
			return true;
		}
		return false;
	}
	
	

}