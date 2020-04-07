words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

print()


"""
Vacio
"""
print("-----------------------------------------\nLista Vacias\n-----------------------------------------")
empty_list = []
print(empty_list)

print()

"""
Lista dentro de otra lista
"""
print("-----------------------------------------\nLista dentro de otra lista\n-----------------------------------------")
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[0])
print(things[1])
print(things[2])
print(things[2][2])
print(things[3])

print()

"""
Texto
"""
print("-----------------------------------------\nLista de Texto\n-----------------------------------------")
str = "Hello world!"
print(str[0],str[1])

print()

"""
Operaciones con Listas
"""
print("-----------------------------------------\nOperaciones con Listas\n-----------------------------------------")
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

print()

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

print()

"""
Para verificar si un elemento está en una lista, se puede usar el operador in. Devuelve True si el elemento aparece una o más veces en la lista y False si no lo hace.
"""
print("-----------------------------------------\nComprobacion de datos en Listas\n-----------------------------------------")
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

print()

"""
Funciones
"""
print("-----------------------------------------\nFunciones en Listas\n-----------------------------------------")

"""
Otra forma de alterar las listas es usar el método append. Esto agrega un elemento al final de una lista existente.
"""
nums = [1, 2, 3]
nums.append(4)#Añadimos
print(nums)


"""
Para obtener el número de elementos en una lista, puede usar la función len.
"""
nums = [1, 3, 5, 2, 4,7]
print(len(nums))


"""
El método de inserción es similar a agregar, excepto que le permite insertar un nuevo elemento en cualquier posición de la lista, en lugar de solo al final.
"""
words = ["Python", "fun"]
words.insert(1, "is")
print(words)


"""
El método de índice encuentra la primera aparición de un elemento de la lista y devuelve su índice.
Si el elemento no está en la lista, genera un ValueError.
"""
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))


