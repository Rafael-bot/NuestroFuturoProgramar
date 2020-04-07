"""
Raising Exceptions

Puede generar excepciones mediante el uso de la declaración de aumento.
"""
try:
  print(1/0)
except ZeroDivisionError:
  raise ValueError

print()

"""
En los bloques excepto, la declaración raise puede usarse sin argumentos para volver a subir cualquier excepción ocurrida.
"""
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise