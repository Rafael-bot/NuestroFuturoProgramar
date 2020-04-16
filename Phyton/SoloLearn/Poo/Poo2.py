class Coche():

    #Constructor
    def ini(self):
        self.__asientos = 4 #Encapsulamiento
        self.__altura = 3.0
        self.__anchura = 5.0
        self.__ruedas = 4
        self.__enmarcha = False
        self.__marca = "Opel"
        self.__modelo = "89-VG"

    #Metodos
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            check = self.__chequeo()

        if self.__enmarcha and check: #Si la variable __enmarcha es true y el chekeo es true entonces el coche se pondara en marcha
            return "El coche esta en marcha."

        elif self.__enmarcha and check == False:
            return "El coche esta mal."

        elif self.__enmarcha == "False":
            return "El coche esta parado."

    def estado(self):
        print("El coche tiene ",self.__ruedas," ruedas. Un ancho de ",self.__anchura," y un largo de ",self.__altura,".")

    def __chequeo(self):#Encapsulamos el metodo, es decir, cualquier metodo encapsulado no se podra acceder a el desde fuera. Uilizamos la dobles barras bajas.

        self.__gasolina = "Ok"
        self.__aceite = "Ok"
        self.__puerta = "Cerradas"

        if self.__gasolina == "Ok" and self.__aceite == "Ok" and self.__puerta == "Cerradas":
            return True
        else:
            return False

micoche1 = Coche()
micoche1.ini()
micoche1.estado()
print(micoche1.arrancar(True))

print()
micoche2 = Coche()
micoche2.ini()
micoche2.estado()
print(micoche2.arrancar(False))