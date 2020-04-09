"""
List Slices

Los sectores de lista proporcionan una forma más avanzada de recuperar valores de una lista. La división básica de listas implica indexar una lista con dos enteros separados por dos puntos. Esto devuelve una nueva lista que contiene todos los valores de la lista anterior entre los índices.
"""
print("-----------------------------------------\nList Slices\n-----------------------------------------")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[0:3])
print(squares[3:-1])#Los valores negativos se pueden usar en el corte de la lista (y la indexación de la lista normal). Cuando se usan valores negativos para el primer y el segundo valor en un segmento (o un índice normal), cuentan desde el final de la lista.
print(squares[0:1])

print()

"""
Si se omite el primer número en un segmento, se considera que es el comienzo de la lista.
Si se omite el segundo número, se considera que es el final.
"""
triangule = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(triangule[:7])#imprime todos los valores que estan debajo de la posicion indicada.
print(triangule[7:])#Imprime todos los numeros todos lo valores que estan delante de del valor que esta en la posición indicada incluyendolo.

print()

"""
Los sectores de la lista también pueden tener un tercer número, que representa el paso, para incluir solo valores alternativos en el sector.
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])