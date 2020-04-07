"""
Rango

La función de rango crea una lista secuencial de números.
El siguiente código genera una lista que contiene todos los enteros, hasta 10.
"""
print("-----------------------------------------\nRango\n-----------------------------------------")
numbers = list(range(10))
print(numbers)
nums = list(range(5))
print(nums[4])

print()

"""
Si se llama a range con un argumento, produce un objeto con valores de 0 a ese argumento.
Si se llama con dos argumentos, produce valores del primero al segundo.
"""
print("-----------------------------------------\nRango Con 2 Argumentos\n-----------------------------------------")
numbers = list(range(3, 8))
print(numbers)
print(range(20) == range(0, 20))

print()

"""
El rango puede tener un tercer argumento, que determina el intervalo de la secuencia producida. Este tercer argumento debe ser un número entero.
"""
print("-----------------------------------------\nRango Con 3 Argumentos\n-----------------------------------------")
numbers = list(range(5, 20, 1))#El Tercer argumento es de cuanto es la cantidad de conteo
print(numbers)

