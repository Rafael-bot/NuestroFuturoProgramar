package Herencias.Clases;

public class Caducado extends Producto{
	
	public int dias_caducidad;
		
	public Caducado(String nombre, double precio, int dias_caducidad) {
		super(nombre, precio);
		this.dias_caducidad = dias_caducidad;
	}

	public int getDias_caducidad() {
		return this.dias_caducidad;
	}
	
	public void setDias_caducidad(int dias_caducidad) {
		this.dias_caducidad = dias_caducidad;
	}
	
	@Override
	public String toString() {
		return super.toString()+"Tiempo"+"dias_caducidad"+dias_caducidad;
	}
	
	@Override
	public double calcular(int cantidad) {
		
		double precioFinal = super.calcular(cantidad);
		
		switch (dias_caducidad) {
		case 1:
			precioFinal /= 4;
			break;

		case 2:
			precioFinal /= 3;
			break;

		case 3:
			precioFinal /= 2;
			break;
		}
		return precioFinal;
	}
	
}
