package Herencias.Clases;

public class Persona {
	
	public String nombre;
	
	public Persona() {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
		}
	
	public Persona(String nombre) {
		this.nombre = nombre;
		System.out.println("Constructor Persona");
	}
	
	public String getNombre() {//lo que tengo
		return this.nombre;
	}
	
	public void setNombre(String nombre) {// para editarlo
		this.nombre = nombre;
		
	}
	
	@Override
	public String toString() {
		return "Persona: "+nombre; 
	}
	
}
