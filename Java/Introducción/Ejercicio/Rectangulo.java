package Introducción.Ejercicio;

import Introducción.Ejercicio.Clase.claseRectanguloDatos;
import Introducción.Ejercicio.Clase.clasesRectanguloFormula;

public class Rectangulo {

	public static void main(String[] args) {
		claseRectanguloDatos datos = new claseRectanguloDatos();
		clasesRectanguloFormula formula = new clasesRectanguloFormula();
		
		datos.altura = 1.3;
		datos.anchura = 2.5;
		
		System.out.println("------------------------------------------------");
		System.out.println("\t El area es "+formula.area(datos.altura, datos.anchura)+".");
		System.out.println("\t El Perimetro es "+formula.perimetro(datos.altura, datos.anchura)+".");
		System.out.println("-------------------------------------------------");
		
	}

}
