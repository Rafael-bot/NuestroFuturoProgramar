
"""
Concatenación

Al igual que con los enteros y flotantes, se pueden agregar cadenas en Python, utilizando un proceso llamado concatenación, que se puede hacer en cualquiera de las dos cadenas.
Al concatenar cadenas, no importa si se han creado con comillas simples o dobles.

"""
print("-----------------------------------------\nConcatenación\n-----------------------------------------")

print()

print("Texto")
print("Raf" + 'ael')
print("First string" + ", " + "second string")

print()

print("Numeros")
print("2" + "2")
#print(1 + '2' + 3 + '4) #La concatenación es para el tipo string

print()

"""
Operaciones de String

Las cadenas también se pueden multiplicar por enteros. Esto produce una versión repetida de la cadena original. El orden de la cadena y el número entero no importa, pero la cadena generalmente viene primero.

Las cadenas no se pueden multiplicar por otras cadenas. Las cadenas tampoco pueden multiplicarse por flotadores, incluso si los flotadores son números enteros.

"""
print("-----------------------------------------\nConcatenación\n-----------------------------------------")

print()

print("spam " * 3)#El numero por el que multiplica se puede poner tanto delante como detras, y tiene que ser tipo int
print(4 * '2')
#print('17' * '87')#Error, ya que  no se puede ,ultiplicar dos string
