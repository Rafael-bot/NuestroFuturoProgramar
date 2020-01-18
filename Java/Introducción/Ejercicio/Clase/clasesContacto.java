package Introducción.Ejercicio.Clase;

import Introducción.Ejercicio.Movil;
import Introducción.Ejercicio.Clase.clasesAgenda;


public class clasesContacto{
	String nombre;
	String telefono;

	public clasesContacto(){
		this("Desconocido", null);
	}
	public clasesContacto(String nombre){
		this(nombre, null);
	}
	public clasesContacto(String nombre, String telefono){
		this.nombre = nombre;
		this.telefono = telefono;
	}
	public clasesContacto(String nombre, int telefono){
		this(nombre, String.valueOf(telefono));
	}

	public String getNombre(){
		return this.nombre;
	}
	public String getTelefono(){
		return this.telefono;
	}

	public void setNombre(String nombre){
		this.nombre = nombre;
	}
	public void setTelefono(String telefono){
		this.telefono = telefono;
	}

	public void llamar(){}
	public void colgar(){}
}     