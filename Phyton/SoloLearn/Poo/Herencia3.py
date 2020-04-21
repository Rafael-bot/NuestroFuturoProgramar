#Super
class Persona():

    def __init__(self, nombre, apellido1, apellido2, edad, lugar_residencia):
         self.nombre = nombre
         self.apellido1 = apellido1
         self.apellido2 = apellido2
         self.edad = edad
         self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print(
            " Nombre: ",self.nombre,
            "\n Apellidos: ",self.apellido1+" "+self.apellido2,
            "\n Edad: ",self.edad,
            "\n Lugar de Residencia: ",self.lugar_residencia
        )

class Empleado(Persona):

    def __init__(self,nomb_empleado, ape1_empleado, ape2_empleado, edad_empleado, lugresidenc_empleado,salario, antiguedad):
        super().__init__(nomb_empleado, ape1_empleado,ape2_empleado, edad_empleado, lugresidenc_empleado)#Estamos inicializando las variable de la clase persona
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()#Esta ejecutando el metodo descripcion de la clase Persona
        print(
            " Salario: ",self.salario,
            "\n Antiguedad: ",self.antiguedad
        )

per1 = Persona("Fran","Rebollo","Rivera",24,"Sevilla")
per1.descripcion()
print(isinstance(per1,Persona))#Estamos comprobando si esta en la clase. Si sale true es que esta y si sale false es que no esta.
print(isinstance(per1,Empleado))
print()

per2 = Empleado("Antonio","Garcia","Rivera",32,"Madrid",857,2)
per2.descripcion()
print(isinstance(per2,Persona))
print(isinstance(per2,Empleado))


