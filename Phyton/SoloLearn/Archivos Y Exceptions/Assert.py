"""
Assertions

Una assertion es un control de cordura que puede activar o desactivar cuando haya terminado de probar el programa.
Se prueba una expresión y, si el resultado es falso, se genera una excepción.
Las afirmaciones se llevan a cabo mediante el uso de la declaración de assert.
"""
a = 2
b = 3
print("Bienvenido")
assert a+b==5
print(a+b)
assert a+b==0
print(0)

print()

"""
La aserción puede tomar un segundo argumento que se pasa al AssertionError generado si la aserción falla.
"""
x = 10
z = 12
assert (x>z),"Z mayor que X"
print("Gracias")

def myfunc(x):
    assert x>0,"Error!"
    print(x)
myfunc(4)

