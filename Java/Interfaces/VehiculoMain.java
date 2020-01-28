package Interfaces;

import Interfaces.Clases.*;

public class VehiculoMain {

	public static void main(String[] args) {
		Parking park = new Parking(200,true);
		Coche coch = new Coche();
		
		coch.hayPlaza(park.hayplazas);	
		coch.Aparca(park.hayplazas);
		
		if (park.hayplazas == true) {
			System.out.println(park.factura());
			park.setTiempo();
		}
		

	}

}


/*

20.9.1 EJERCICIO 37
Desarrollar una interfaz Vehiculo que declare los métodos factura(), hayPlaza(), aparca() y setTiempo(), tales que:

factura() proporciona el importe a pagar por estacionar un Vehiculo durante un tiempo determinado en el parking.

hayPlaza() recibe como argumento una referencia a un objeto Parking y determina si hay sitio en dicho parking para estacionar un Vehiculo.

aparca() recibe como argumento una referencia a un objeto Parking y estaciona un Vehiculo en dicho parking.

setTiempo() recibe como argumento un entero y establece ese entero como tiempo de estancia del Vehiculo en el Parking.

*/