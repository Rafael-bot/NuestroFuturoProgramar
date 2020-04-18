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
            print("Eres español.")

    def estado(self):
        print(
            "Nombre: ",self.nombre,
            "\nApellidos: ",self.apellido1+" "+self.apellido2,
            "\nLocalidad: ",self.localidad,
            "\nEdad: ",self.edad,
            "\n¿Tiene coche? ",self.coche,
        )

class Niño(Personas):

    def parque(self):
        if self.edad <= 10:
            self.bingo = "Voy al parque."

        else:
            self.bingo = "Eso es de niños chicos."

    def estado(self):
        print(
            "Nombre: ",self.nombre,
            "\nApellidos: ",self.apellido1+" "+self.apellido2,
            "\nLocalidad: ",self.localidad,
            "\nEdad: ",self.edad,
            "\n¿Tiene coche? ",self.coche,
        )

class Viejo(Personas):# Aquí le estamos indicando que la clase Viejo va a heredar los metodos de la clase Personas.

    def bing(self):
        if self.edad >= 60:
            self.bingo = "Voy al bingo."

        else:
            self.bingo = "Eso es para viejos."

    def estado(self):#Estamos sobbreescribiendo el metodo estado de la clase Personas. A que llamarlo igual
        print(
            "Nombre: ", self.nombre,
            "\nApellidos: ", self.apellido1 + " " + self.apellido2,
            "\nLocalidad: ", self.localidad,
            "\nEdad: ", self.edad,
            "\n¿Tiene coche? ", self.coche,
            "\nViejo: ",self.bingo
        )

class Joven():

    def __init__(self):
        self.deporte = 100
    def cargando(self):
        self.cargando = True

class Vida(Personas,Joven):#Cuando hay herencia multiple se da preferancia al primer argumento, es decir, a la primera clase
    pass

per1 = Personas("Juan","Oliva","Ramirez",60,"España")
per1.estado()

print()

per2 = Viejo("Juan","Oliva","Ramirez",60,"España")
per2.bing()
per2.estado()

print()

per3 = Niño("Juan","Oliva","Ramirez",60,"España")
per3.parque()
per3.estado()

print()

per4 = Vida("Juan","Oliva","Ramirez",60,"España")
per4.estado()

