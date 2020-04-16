class Coche():
    #Prpiedades
    def iniciar(self):#Creamos un metodo para inciar todas las propiedades
        self.__altura=3.00
        self.__anchura=6.00
        self.__asientos = 4 #La encapsulamos con dos barras bajas despues del punto, es decir solo es accesible dentro de la propia clase
        self.enmarcha = False

    #Metodo
    def arrancar (self,arrancamos):# self es igual this
        self.enmarcha = arrancamos
        if self.enmarcha:
            print("Esta en marcha")
        else:
            print("Esta parado")
    def estado(self):
        print("El coche tiene 4 Ruedas y ",self.__asientos," asientos.")

#Inicializamos
micoche1 = Coche()
micoche2 = Coche()

print("Coche 1")
#Variable
print(micoche1.iniciar())
#Ejecutamos el metodo
micoche1.arrancar(True)
micoche1.estado()

print()

print("Coche 2")
#Variable
print(micoche2.iniciar())
#Ejecutamos el metodo
micoche2.arrancar(False)
micoche2.estado()