package Interfaces.Clases;

import Interfaces.*;

public class Gato implements Animal{
	
	public String nombre;

	public Gato(String nombre) {
		this.nombre = nombre;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	public void saludar(Animal perro) {
		System.out.println("Miau Miau Miau");
	}	
	
	public void saludar() {
		System.out.println("Miauuu");
	}
	
	@Override
	public String toString() {
		return "Gato nombre: " + nombre;
	}
	
	
	
	
	
}
