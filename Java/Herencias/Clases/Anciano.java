package Herencias.Clases;

public class Anciano extends Persona{
	
	public Anciano() {
		this("Anciano");
	}
	public Anciano(String nombre) {
		super(nombre);//Llama a constructor padre
		System.out.println("Constructor Anciano");
	}
	
	@Override
	public String toString() {
		return super.toString()+" -> Anciano"; 
	}

}
