package Introducción.Ejercicio;

import Introducción.Ejercicio.Clase.clasePersona;;

public class Persona {

	public static void main(String[] args) {
		clasePersona persona = new clasePersona();//Instanciar objeto
		
		//Inicializar variable
		clasePersona.nombre = "Rafael";
		clasePersona.edad = 18;
		clasePersona.altura = (float) 1.75;
		//clasePersona.mayoredad = true;
		clasePersona.dni = "30247808H";
		
		//Usar variables y metodos
		System.out.println(clasePersona.nombre);
		
		System.out.println();
		System.out.println(clasePersona.edad);
		System.out.print("Mayor de edad: ");System.out.println(clasePersona.mayoredad());
		
		System.out.println();
		System.out.println(clasePersona.altura);
		
		System.out.println();
		System.out.println(clasePersona.dni);
		System.out.print("Esta dni es valido: ");System.out.println(clasePersona.rangodni());
		

	}

}
