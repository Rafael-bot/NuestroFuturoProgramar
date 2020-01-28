package Ejercicios;

import Ejercicios.Clases.*;

public class BotellaMain {

	public static void main(String[] args) {
		
		String [] marca = {"Botoa","Cosasd","KOko","Vock"};
		float [] capacidad = {1,2,1,1};
		double [] gradoAlc = {15.7,6,12.9,5.6};
		
		Botella bot = new Botella(marca, capacidad, gradoAlc);
		Acción acc = new Acción(marca, capacidad, gradoAlc);
		
		bot.Marca(3);
		bot.Capacidad(3);
		
		acc.Serv(30);		
		acc.Vaciar();
		acc.Llenar();
		
	}

}
