package Herencias.Clases;

public class Joven extends Persona{
	
	public Joven() {
		this("Joven");
	}
	public Joven(String nombre) {
		super(nombre);//Llama a constructor padre
		System.out.println("Constructor Jovene");
	}
	
	@Override
	public String toString() {
		return super.toString()+" -> Joven"; 
	}

}
