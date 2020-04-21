class Coche():

    def desplazamiento(self):
        print("Me estoy deplazando en coche.")

class Moto():
    def desplazamiento(self):
        print("Me estoy deplazando en moto.")

class Camion():
    def desplazamiento(self):
        print("Me estoy deplazando en camion.")

#Sin polimorfismo
v1 = Coche()
v2 = Moto()
v3 = Camion()

v1.desplazamiento()
v2.desplazamiento()
v3.desplazamiento()

print()

#Con polimorfismo
def despvehiculo(vehiculo):#Va ha ejecutar el metodo desplazamiento de la clase que le intorduzcas.
    vehiculo.desplazamiento()

vp1 = Coche()
vp2 = Moto()
vp3 = Camion()

despvehiculo(vp1)
despvehiculo(vp2)
despvehiculo(vp3)

