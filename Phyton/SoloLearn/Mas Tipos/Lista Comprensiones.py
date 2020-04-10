"""
Lista de comprensiones

Las comprensiones de listas son una forma útil de crear rápidamente listas cuyos contenidos obedecen a una regla simple.
"""
print("-----------------------------------------\nLista de Compresion\n-----------------------------------------")
cubes = [i**3 for i in range(5)]
print(cubes)

print()

"""
Una comprensión de la lista también puede contener una instrucción if para imponer una condición en los valores de la lista.
"""
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
a = [i for i in range(20) if i%3==0]
print(a)

print()

"""
Intentar crear una lista en un rango muy extenso resultará en un error de memoria.
Este código muestra un ejemplo donde la comprensión de la lista se queda sin memoria.
"""
even = [2*i for i in range(10**100)]
print(even)



