class Personas():

    def __init__(self, nombre, apellido1, apellido2, edad, localidad):
         self.nombre = nombre
         self.apellido1 = apellido1
         self.apellido2 = apellido2
         self.localidad = localidad
         self.edad = edad
         self.mayoredad = False
         self.coche = False
         self.español = False

    def mayoredad(self):
        self.mayoredad = True
        print("Eres mayor de edad.")

    def coche(self):
        if self.mayoredad:
            self.coche = True
            print("Tienes coche.")

        else:
            self.coche = False
            print("No puedes tener coche.")

    def español(self):
        if self.localidad == "España":
            self.español = True
            print("Eres espñol.")

    def estado(self):
        print(
            "Nombre: ",self.nombre,
            "\nApellidos: ",self.apellido1+" "+self.apellido2,
            "\nLocalidad: ",self.localidad,
            "\nEdad: ",self.edad,
            "\n¿Tiene coche? ",self.coche
        )

class Viejo(Personas):# Aquí le estamos indicando que la clase Viejo va a heredar los metodos de la clase Personas.
    pass

per1 = Viejo("Juan","Oliva","Ramirez",60,"España")
per1.estado()