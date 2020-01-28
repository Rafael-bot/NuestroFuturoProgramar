package Herencias.Clases;

public class Adulto extends Persona{//Con el extends le indicamos que persona es el archivo padre
	
	public Adulto() {
		this("Adulto");
	}
	public Adulto(String nombre) {
		super(nombre);//Llama a constructor padre
		System.out.println("Constructor Adulto");
	}
	
	@Override
	public String toString() {
		return super.toString()+" -> Adulto"; 
	}
	
	
}
