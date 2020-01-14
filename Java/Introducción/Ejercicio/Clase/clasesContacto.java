package Introducción.Ejercicio.Clase;

public class clasesContacto {
	
		//Contacto
		public static String[] nombre = {"Rafael","Javier","Vladimir","Donald","Cristian"};// Es el nombre del movil		
		public static int[] telefono = {954455721,617548989,613234596,632157548,612345786};// Es el numero del movil que es un contacto
		public static void recorridocontact() {
			for (int cont = 0; cont < 5; cont++) {
				System.out.println("|\t +"+nombre[cont]+"\t         |");
				System.out.println("|\t\t -"+telefono[cont]+"\t |");
			}
		}
				
		public static String llamar() {//Acción (llamas a un contacto de agenda)
			return añadir;
		}
		public static String colgar;//Acción (cuelgas a un contacto que has llamado)
		
		
		
		

		

	

		
		
	
}
