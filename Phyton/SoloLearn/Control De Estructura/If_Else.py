"""
If

Puede usar sentencias if para ejecutar código si se cumple una determinada condición.
Si una expresión se evalúa como True, se llevan a cabo algunas declaraciones. De lo contrario, no se llevan a cabo.

"""
print("-----------------------------------------\nIf\n-----------------------------------------")

if 10 > 5:#Condicion
   print("10 es mayor que 5")#Accion si se cumple la acción

spam = 7
if spam > 5:#Se cumple la primera condición
   print("five")
if spam > 8:
   print("eight")

print()

"""
Else

Una instrucción else sigue a una instrucción if y contiene un código que se llama cuando la instrucción if se evalúa como False.
Al igual que con las declaraciones if, el código dentro del bloque debe estar sangrado.

"""

print("-----------------------------------------\nElse\n-----------------------------------------")

x = 4
if x == 5:
   print("Yes")
else:
   print("No")

print()

"""
Elif

La declaración elif (abreviatura de else if) es un atajo para usar al encadenar declaraciones if y else.
Una serie de sentencias if elif puede tener un bloque else más, que se llama si ninguna de las expresiones if o elif es True.

"""
print("-----------------------------------------\nElif\n-----------------------------------------")

num = 7
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")