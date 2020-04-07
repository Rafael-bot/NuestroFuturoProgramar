"""
Boolean Logic

La lógica booleana se usa para crear condiciones más complicadas para sentencias if que se basan en más de una condición.
Los operadores booleanos de Python son y, o, y no.
El operador y toma dos argumentos y se evalúa como Verdadero si, y solo si, sus dos argumentos son Verdaderos. De lo contrario, se evalúa como False.

"""
print("-----------------------------------------\nBoolean Logic(and)\n-----------------------------------------")

print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 >  6)
if (1 == 1) and (2 + 2 > 3):
  print("true")
else:
  print("false")

print()

"""

Boolean Or
El operador o también toma dos argumentos. Se evalúa como Verdadero si alguno (o ambos) de sus argumentos son Verdaderos y Falso si ambos argumentos son Falso.

"""
print("-----------------------------------------\nBoolean Logic(or)\n-----------------------------------------")

print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 == 1 or 2 == 3)
print(2 < 1 or 3 >  6)

print()

"""

Boolean Not
A diferencia de otros operadores que hemos visto hasta ahora, no solo toma un argumento y lo invierte.
El resultado de no Verdadero es Falso, y no Falso va a Verdadero.

"""
print("-----------------------------------------\nBoolean Logic(not)\n-----------------------------------------")

print(not 1 == 1)
print(not 1 > 7)
if not True:
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")