"""
Funciones de cuerda

Python contiene muchas funciones y métodos integrados útiles para realizar tareas comunes.
- join: une una lista de cadenas con otra cadena como separador.
- remplace: reemplaza una subcadena en una cadena por otra.
- startswith and endswith: determine si hay una subcadena al comienzo y al final de una cadena, respectivamente.
- Para cambiar el caso de una cadena, puede usar lower y upper.
- El método split es el opuesto de join, convirtiendo una cadena con cierto separador en una lista.
"""
print("er ".join(["spam", "eggs", "ham"]))# Unicamente entre valores
#prints "spam, eggs, ham"

print("Hola Rafael".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"
print("Sentence is a sentence this.".startswith("This"))
# prints "False"

print("This is a sentence.".endswith("sentence."))
# prints "True"
print("Sentence is a sentence this.".endswith("sentence."))
# prints "False"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

print()

"""
Funciones numéricas

Para encontrar el máximo o mínimo de algunos números o una lista, puede usar max o min.
Para encontrar la distancia de un número desde cero (su valor absoluto), use abs.
Para redondear un número a un cierto número de decimales, use round.
Para encontrar el total de una lista, use sum.
"""
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))

print(abs(-99))
print(abs(42))

print(round(3.999))

print(sum([1, 2, 3, 4, 5]))

print()

"""
Funciones de lista

A menudo se usa en declaraciones condicionales, all  y any  uno toman una lista como argumento y devuelven True  si todos o alguno (respectivamente) de sus argumentos se evalúan como True  (y False de lo contrario).
La función enumerate  se puede usar para recorrer los valores e índices de una lista
"""
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for cont in enumerate(nums):
    print(cont)


