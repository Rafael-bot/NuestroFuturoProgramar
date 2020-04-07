"""
Módulos

Los módulos son piezas de código que otras personas han escrito para cumplir tareas comunes, como generar números aleatorios, realizar operaciones matemáticas, etc.

La forma básica de usar un módulo es agregar import module_name en la parte superior de su código, y luego usar module_name.var para acceder a funciones y valores con el nombre var en el módulo.
"""

import random# Con el import importamos los modulos, en este caso hemos importado el random

for i in range(5):
   value = random.randint(1, 6)
   print(value)

print()

"""
Hay otro tipo de importación que puede usarse si solo necesita ciertas funciones de un módulo.
Estos toman la forma de module_name import var, y luego var se puede usar como si estuviera definido normalmente en su código.
"""
from math import pi,sqrt# Hemos importado de la libreria math el modulo pi. Si ponemos una coma despues de un modulo podemos añadir otro modulos y así con todos

print(pi)
print(sqrt(2))

print()

"""
Puede importar un módulo u objeto con un nombre diferente utilizando la palabra clave as. Esto se usa principalmente cuando un módulo u objeto tiene un nombre largo o confuso.
"""
from math import sqrt as square_root#Con el AS le podemos un alias al modulos
print(square_root(100))

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))

