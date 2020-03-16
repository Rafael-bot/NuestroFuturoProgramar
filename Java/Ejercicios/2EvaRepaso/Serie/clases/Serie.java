package Serie.clases;

public class Serie implements Entregable{
	
	//Atributos
	private String titulo;
	private String creador;
	private int temporadas = 3;
	private Boolean entregado = false;
	private String genero;
	
	
	//Constructores
	public Serie() {}//Por defecto
	public Serie(String titulo, String creador) {//Constructor Titulo y Creador
		this.titulo = titulo;
		this.creador = creador;
	}
	public Serie(String titulo, String creador, int temporadas, String genero) {//Constructor Excepto entregado
		this.titulo = titulo;
		this.creador = creador;
		this.temporadas = temporadas;
		this.genero = genero;
	}
	
	
	//Get y Set
	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	public String getCreador() {
		return creador;
	}
	public void setCreador(String creador) {
		this.creador = creador;
	}
	public int getTemporadas() {
		return temporadas;
	}
	public void setTemporadas(int temporadas) {
		this.temporadas = temporadas;
	}
	public String getGenero() {
		return genero;
	}
	public void setGenero(String genero) {
		this.genero = genero;
	}
	
	
	//Metodos
	@Override
	public String toString() {
		return "Informacion de la Serie: \n" +
                "\tTitulo: "+titulo+"\n" +
                "\tNumero de temporadas: "+temporadas+"\n" +
                "\tGenero: "+genero+"\n" +
                "\tCreador: "+creador;
	}
	
	public boolean entregar() {
		return this.entregado=true;
	}
	
	public boolean devolver() {
		return this.entregado=false;
	}
	
	public boolean isEntregado() {
		return this.entregado;
	}
	
	
	
}
