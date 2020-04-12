"""
Lambdas

Crear una función normalmente (usando def) la asigna a una variable automáticamente.
Esto es diferente de la creación de otros objetos, como cadenas y enteros, que se pueden crear sobre la marcha, sin asignarlos a una variable.
Lo mismo es posible con las funciones, siempre que se creen utilizando la sintaxis lambda. Las funciones creadas de esta manera se conocen como anónimas.
Este enfoque se usa más comúnmente cuando se pasa una función simple como argumento a otra función. La sintaxis se muestra en el siguiente ejemplo y consiste en la palabra clave lambda seguida de una lista de argumentos, dos puntos y la expresión para evaluar y devolver.
"""
def my_func(f, arg):
  return f(arg)
print(my_func(lambda x: 3*x, 4))

print()

"""
Las funciones de Lambda no son tan poderosas como las funciones con nombre.
Solo pueden hacer cosas que requieren una sola expresión, generalmente equivalente a una sola línea de código.
"""
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

print()

"""
Las funciones Lambda pueden asignarse a variables y usarse como funciones normales.
"""
double = lambda x: x * 2
print(double(2))

