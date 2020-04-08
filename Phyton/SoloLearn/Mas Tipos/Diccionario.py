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
print(primary["yellow"])

print()

"""
Solo los objetos inmutables pueden usarse como claves para los diccionarios. Los objetos inmutables son aquellos que no se pueden cambiar. Hasta ahora, los únicos objetos mutables con los que te has encontrado son listas y diccionarios. Intentar utilizar un objeto mutable como clave de diccionario provoca un TypeError.
"""
bad_dict = {
  [1, 2, 3]: "one two three",
}

print()

"""

"""
print("-----------------------------------------\nFunciones de Diccionarios\n-----------------------------------------")
