"""
Conversión de tipo

En Python, es imposible completar ciertas operaciones debido a los tipos involucrados.
Por ejemplo, no puede agregar dos cadenas que contengan los números 2 y 3 juntos para producir el número entero 5, ya que la operación se realizará en cadenas, haciendo que el resultado sea '23'.
La solución a esto es la conversión de tipos.
En ese ejemplo, usaría la función int.

"""
print("-----------------------------------------\nConversión_de_tipo\n-----------------------------------------")

print()

print("2" + "3")#Aqui estamos concatenamos los dos String
print(int("2") + int("3"))#Aqui estamos sumando el 2 y el 3, ya que estamos convirtiendo los string en int

#print(int("3" + "4"))#No convierte

print()

"""

Otro ejemplo de conversión de tipo es convertir la entrada del usuario (que es una cadena) en números (enteros o flotantes), para permitir el desempeño de los cálculos.

"""

print( float(input("Enter a number: ")) + float(input("Enter another number: ")))


