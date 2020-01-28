package Interfaces.Clases;

import Interfaces.*;

public class Perro implements Animal{//Con "implements" le indicamos donde estan la interface.
	
	public String nombre;

	public Perro(String nombre) {
		this.nombre = nombre;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
		
	public void saludar(Animal gato) {
		System.out.println("Guau Guau Guau");
	}
	
	public void saludar() {//Requisito
		System.out.println("Guauu");
	}

	@Override
	public String toString() {
		return "Perro nombre: " + nombre;
	}
	
	
	
	
	
}
