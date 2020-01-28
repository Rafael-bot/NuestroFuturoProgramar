package Herencias.Clases;

public class NoCaducado extends Producto{


	public String tipo;
	
	public NoCaducado(String nombre, double precio, String tipo) {
		super(nombre, precio);
		this.tipo = tipo;
	}
	
	public String getTipo() {
		return this.tipo;
	}
	
	public void SetTipo(String tipo) {
		this.tipo = tipo;
	}
	
	@Override
	public String toString() {
		return super.toString()+"tipo"+tipo;
	}
	
	
}
