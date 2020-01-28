package Interfaces.Clases;

public class Coche implements Vehiculo{
	
	
	public String aparca;
	
	public Coche() {}

	public String getAparca() {
		return aparca;
	}

	public void setAparca(String aparca) {
		this.aparca = aparca;
	}
	
	@Override
	public void Aparca(boolean ap) {
		if (ap == true) {
			System.out.println("Estoy aparcando");
		}
		
	}

	@Override
	public void hayPlaza(boolean plazas) {
		
		if (plazas == true) {
			System.out.println("Se puede aparcar");
		} else {
			System.out.println("Lo siento, intentalo otra vez");
		}
		
	}
	}
	
	
	
	



/*
aparca() recibe como argumento una referencia a un objeto Parking y estaciona un Vehiculo en dicho parking.

hayPlaza() recibe como argumento una referencia a un objeto Parking y determina si hay sitio en dicho parking para estacionar un Vehiculo.
*/