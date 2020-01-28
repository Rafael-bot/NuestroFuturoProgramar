package Herencias.Clases;

public class Producto {
	
	public String nombre;//Creamos las variables.
	public double precio;
	
	public Producto(String nombre, double precio) {
		super();
		this.nombre = nombre;
		this.precio = precio;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

	@Override
	public String toString() {
		return "nombre" + nombre+", precio"+precio;
	}
	
	
	public double calcular(int cantidad) {//Polimorfirmo es que el metodo se crear tanto en el padre como en todos los hijos.
		return precio*cantidad;
		
	}
	
	
	
}
