package Serie.clases;

import javax.print.attribute.standard.PresentationDirection;

public class Videojuego implements Entregable{
	
	//Atributos
	private String titulo;
	private int horas = 10;
	private boolean entregado = false;
	private String genero;
	private String compa�ia;
	
	//Constructores
		public Videojuego() {}//Por defecto

		public Videojuego(String titulo, int horas) {//Const Titulo y Horas
			this.titulo = titulo;
			this.horas = horas;
		}

		public Videojuego(String titulo, int horas, String genero, String compa�ia) {//Const tiutlo, horas, genero, compa�ia
			this.titulo = titulo;
			this.horas = horas;
			this.genero = genero;
			this.compa�ia = compa�ia;
		}

		//Get y Set
		public String getTitulo() {
			return titulo;
		}

		public void setTitulo(String titulo) {
			this.titulo = titulo;
		}

		public int getHoras() {
			return horas;
		}

		public void setHoras(int horas) {
			this.horas = horas;
		}

		public String getGenero() {
			return genero;
		}

		public void setGenero(String genero) {
			this.genero = genero;
		}

		public String getCompa�ia() {
			return compa�ia;
		}

		public void setCompa�ia(String compa�ia) {
			this.compa�ia = compa�ia;
		}
		
		//Metodos
		@Override
		public String toString() {
			return "Informacion del videojuego: \n" +
	                "\tTitulo: "+titulo+"\n" +
	                "\tHoras estimadas: "+horas+"\n" +
	                "\tGenero: "+genero+"\n" +
	                "\tcompa�ia: "+compa�ia;
		}

	
		public boolean entregar() {
			return this.entregado=true;
		}
		
		public boolean devolver() {
			return this.entregado=false;
		}

		
		public boolean isEntregado() {
			// TODO Auto-generated method stub
			return this.entregado;
		}

		
		
		

}
