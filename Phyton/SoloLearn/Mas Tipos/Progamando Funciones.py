"""
Programacion Funcional

La programación funcional es un estilo de programación que (como su nombre indica) se basa en las funciones.
Una parte clave de la programación funcional son las funciones de orden superior. Hemos visto esta idea brevemente en la lección anterior sobre funciones como objetos. Las funciones de orden superior toman otras funciones como argumentos o las devuelven como resultados.
"""
def op(func,arg):
    return  func(func(arg))#Esta repitiendo dos veces
def suma(x):
    return x+5
print(op(suma, 10))

print()

"""
La programación funcional busca utilizar funciones puras. Las funciones puras no tienen efectos secundarios y devuelven un valor que depende solo de sus argumentos.
Así es como funcionan las funciones matemáticas: por ejemplo, cos (x), por el mismo valor de x, siempre devolverá el mismo resultado.

Funciones puras

El uso de funciones puras tiene ventajas y desventajas.
Las funciones puras son:
- Más fácil de razonar y probar.
- más eficiente. Una vez que la función ha sido evaluada para una entrada, el resultado puede almacenarse y referirse a la próxima vez que se necesita la función de esa entrada, reduciendo el número de veces que se llama a la función. Esto se llama memorización.
- Más fácil de ejecutar en paralelo.
"""
#Pura
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
print(pure_function(3,6))

#Impuro
some_list = []
def impure(arg):
  some_list.append(arg)
  return some_list
print(impure(["hola","Adios","Cosa"]))