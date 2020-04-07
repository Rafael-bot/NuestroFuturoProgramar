"""
Manejo de excepciones

Para manejar excepciones y para llamar al código cuando ocurre una excepción, puede usar una declaración try / except.
El bloque try contiene código que puede generar una excepción. Si se produce esa excepción, el código en el bloque try deja de ejecutarse y se ejecuta el código en el bloque except. Si no se produce ningún error, el código en el bloque excepto no se ejecuta.
"""
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done")
except ZeroDivisionError:
   print("Error")

print()

"""
Una instrucción try puede tener múltiples bloques diferentes, excepto para manejar diferentes excepciones.
También se pueden colocar múltiples excepciones en un solo bloque excepto utilizando paréntesis, para que el bloque excepto se encargue de todos ellos.
"""
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

print()

"""
Una declaración de excepción sin ninguna excepción especificada detectará todos los errores. Deben usarse con moderación, ya que pueden detectar errores inesperados y ocultar errores de programación.
"""
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")