package Ejercicios.Clases;

public class Botella implements BotellaInterface{
	
	public String [] Marca;
	public float [] Capacidad;//En  milimetro
	public double [] GradoAlc;// Marca
	public byte PorcentLlenado;// Capacidad
	
	public Botella(String[] marca, float[] capacidad, double[] gradoAlc) {

		this.Marca = marca;
		this.Capacidad = capacidad;
		this.GradoAlc = gradoAlc;
		this.PorcentLlenado = 100;
	}


	public String[] getMarca() {
		return Marca;
	}

	public void setMarca(String[] marca) {
		Marca = marca;
	}

	public float[] getCapacidad() {
		return Capacidad;
	}

	public void setCapacidad(float[] capacidad) {
		Capacidad = capacidad;
	}

	public double[] getGradoAlc() {
		return GradoAlc;
	}

	public void setGradoAlc(double[] gradoAlc) {
		GradoAlc = gradoAlc;
	}

	public double getPorcentLlenado() {
		return PorcentLlenado;
	}

	public void setPorcentLlenado(byte porcentLlenado) {
		PorcentLlenado = porcentLlenado;
	}

	//Accion
	public void Llenar() {}
	public void Vaciar() {}
	public void Serv() {}
	
	
	
	@Override
	public void Marca(int num) {
		System.out.println("Toma aquí tienes "+this.Marca[num]+" tiene "+this.GradoAlc[num]+" Grado de Alcohol.");
	}

	@Override
	public void Capacidad(int num) {
		System.out.println("Capacidad: "+this.Capacidad[num]+" Litros.");
		System.out.println("Queda "+this.PorcentLlenado+"%.");
	}



	
	
	
	
	
	
	
	
}
