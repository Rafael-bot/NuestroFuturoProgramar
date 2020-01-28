package Ejercicios.Clases;

import java.util.Arrays;

public class Acción extends Botella{
	
	public Acción(String[] marca, float[] capacidad, double[] gradoAlc) {
		super(marca, capacidad, gradoAlc);
	}
	
	public void Serv(int cant) {
		if (this.PorcentLlenado == 0) {
			System.out.println("Esta vacíaaaa!!!");
		} else {
			this.PorcentLlenado = (byte) (this.PorcentLlenado-cant);
			System.out.println("Solo queda "+this.PorcentLlenado+"%");
		}
	}
	
	@Override
	public void Llenar() {

		if (this.PorcentLlenado == 100) {
			System.out.println("La botella esta llena.");
		} else {
			for (int cont = this.PorcentLlenado; this.PorcentLlenado < 100; this.PorcentLlenado++) {
				System.out.println(this.PorcentLlenado+"%");
			}
			System.out.println("Llenada!!!");
		}
	}

	@Override
	public void Vaciar() {
		for (int cont = this.PorcentLlenado; this.PorcentLlenado > 0; this.PorcentLlenado--) {
			System.out.println(this.PorcentLlenado+"%");
		}
		System.out.println("Vaciada!!!");
	}

	
	

	

	
	
	


	
	
}
