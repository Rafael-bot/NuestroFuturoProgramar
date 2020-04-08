"""
Diccionarios

Los diccionarios son estructuras de datos que se utilizan para asignar claves arbitrarias a valores.
Las listas se pueden considerar como diccionarios con claves enteras dentro de un cierto rango.
Los diccionarios se pueden indexar de la misma manera que las listas, usando corchetes que contienen claves.
"""
print("-----------------------------------------\nDiccionarios\n-----------------------------------------")
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

print()

"""
Intentar indexar una clave que no es parte del diccionario devuelve un KeyError.
"""
primary = {
  "red": [255, 0, 0],
  "green": [0, 255, 0],
  "blue": [0, 0, 255],
}

print(primary["red"])
#print(primary["yellow"])#Error Yellow no esta

print()

"""
Solo los objetos inmutables pueden usarse como claves para los diccionarios. Los objetos inmutables son aquellos que no se pueden cambiar. Hasta ahora, los únicos objetos mutables con los que te has encontrado son listas y diccionarios. Intentar utilizar un objeto mutable como clave de diccionario provoca un TypeError.
"""
"""
bad_dict = {
  [1, 2, 3]: "one two three",
}
"""

print()

"""
Funciones de Diccionarios

Al igual que las listas, las teclas del diccionario se pueden asignar a diferentes valores.
Sin embargo, a diferencia de las listas, a una nueva clave de diccionario también se le puede asignar un valor, no solo los que ya existen.
"""
print("-----------------------------------------\nFunciones de Diccionarios\n-----------------------------------------")
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[5] = 64
squares[3] = 9
print(squares)

print()

"""
Para determinar si una clave está en un diccionario, puede usar in y no en, como puede para una lista.
"""
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

print()

"""
Un método útil de diccionario es get. Hace lo mismo que la indexación, pero si la clave no se encuentra en el diccionario, devuelve otro valor especificado ('None', por defecto).
"""
pairs = {1: "apple",
  "orange": [2, 3, 4],
  True: False,
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))#Si no lo encuentra mostrara None
print(pairs.get(123, "not in dictionary"))#El primer argumento es el valor que queremos buscar, pero si no lo encuentra mostrara lo que pongamos en el segundo argumento
