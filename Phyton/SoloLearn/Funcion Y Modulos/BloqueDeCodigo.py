"""
Las funciones

Además de utilizar funciones predefinidas, puede crear sus propias funciones utilizando la instrucción def.
Aquí hay un ejemplo de una función llamada my_func. No requiere argumentos e imprime "spam" tres veces. Se define y luego se llama. Las declaraciones en la función se ejecutan solo cuando se llama a la función.
"""
print("-----------------------------------------\nBloques de Codigo\n-----------------------------------------")

def my_func():
   print("spam")
   print("spam")
   print("spam")

my_func()#Al llamar al boque de codigo, se tiene que llamar despues de crear el bloque

print()

"""
Argumentos

Todas las definiciones de funciones que hemos visto hasta ahora han sido funciones de cero argumentos, que se llaman con paréntesis vacíos.
Sin embargo, la mayoría de las funciones toman argumentos.
"""
print("-----------------------------------------\nBloque de codigo con Argumentos\n-----------------------------------------")
def palabra(nombre):
   print(nombre+"!")

palabra("Rafael")
palabra("Puto")

print()

"""
You can also define functions with more than one argument; separate them with commas.
"""
def op(x,y):
   print(x+y)
   print(y-x)
   print(y/x)

op(7,8)

print()

"""
Function arguments can be used as variables inside the function definition. However, they cannot be referenced outside of the function's definition. This also applies to other variables created inside a function.
"""
def function(variable):
   variable += 1
   print(variable)

function(5)
#print(variable#Error, la variable ya esta creada dentro del bloque de codigo

print()

"""
Returning from Functions

Ciertas funciones, como int o str, devuelven un valor que se puede usar más adelante.
Para hacer esto para sus funciones definidas, puede usar la declaración return.

para que se imprime se necesita el print
"""
print("-----------------------------------------\nBloque de codigo con Return\n-----------------------------------------")
def max(x, y):
   if x >= y:
      return x
   else:
      return y


print(max(4, 7))
z = max(8, 5)
print(z)

print()

def shortest_string(x, y):
   if len(x) <= len(y):
     return x
   else:
      return y
x = list(range(0,10))
y = list(range(0,5))
print(shortest_string(x,y))

print()

"""
Una vez que devuelve un valor de una función, deja de ejecutarse inmediatamente. Cualquier código después de la declaración de devolución nunca sucederá.
"""
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")#Este print no se ejecutaria

print(add_numbers(4, 5))

print()

"""
Aunque se crean de manera diferente a las variables normales, las funciones son como cualquier otro tipo de valor.
Se pueden asignar y reasignar a variables, y luego hacer referencia a ellos con esos nombres.
"""
print("-----------------------------------------\nBloque de codigo ingresar el bloque de un codigo en una variable\n-----------------------------------------")
def suma(x,y):
   return x+y
op = suma(8,2)
print(op)

print()

"""
Las funciones también se pueden usar como argumentos de otras funciones.
"""
print("-----------------------------------------\nFuncion con argumentos de otra funcion\n-----------------------------------------")

def numsum(x,y):
   return x+y
def doblesumas(func,x,y):
   return func(func(x,y),func(x,y))

num1 = 5
num2 = 5

print(doblesumas(numsum,num1,num2))



