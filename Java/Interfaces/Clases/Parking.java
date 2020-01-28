package Interfaces.Clases;

public class Parking implements Aparcamiento{
	
	public double factura;
	public int set_tiempo;
	public boolean hayplazas;
	
	public Parking(int set_tiempo, boolean hayplazas) {
		this.factura = set_tiempo;
		this.set_tiempo = set_tiempo;
		this.hayplazas = hayplazas;
	}

	public double getFactura() {
		return factura;
	}

	public void setFactura(double factura) {
		this.factura = factura;
	}

	public int getSet_tiempo() {
		return set_tiempo;
	}

	public void setSet_tiempo(int set_tiempo) {
		this.set_tiempo = set_tiempo;
	}

	@Override
	public double factura() {
		
		double fact = 0.0;
		int limit = 25;
		
		for (int cont = 0; cont < this.factura; cont++) {
			if (cont == limit) {
				fact = fact+0.25;
				limit = limit+25;
			}
		}
		
		return fact;
		
	}

	@Override
	public void setTiempo() {
		
		int tiempo = this.set_tiempo;
		System.out.println("Solo puedes estar "+tiempo+" minutos.");
		
	}


}

/*

factura() proporciona el importe a pagar por estacionar un Vehiculo durante un tiempo determinado en el parking.

setTiempo() recibe como argumento un entero y establece ese entero como tiempo de estancia del Vehiculo en el Parking.

*/