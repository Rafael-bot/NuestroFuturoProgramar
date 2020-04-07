"""
Ninguna

El objeto None se usa para representar la ausencia de un valor.
Es similar a nulo en otros lenguajes de programación.
Al igual que otros valores "vacíos", como 0, [] y la cadena vacía, es Falso cuando se convierte en una variable booleana.
Cuando se ingresa en la consola de Python, se muestra como la cadena vacía.
"""
print(None==None)
print(None)

print()

"""
El objeto None es devuelto por cualquier función que no devuelva explícitamente nada más.
"""
def some_func():
  print("Hi!")
  #return "Ads"

var = some_func()
print(var)#la funcion no tiene salida, por eso da None(Vacio)

print()

