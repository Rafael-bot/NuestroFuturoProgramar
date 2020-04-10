"""
Formato de cadena

Hasta ahora, para combinar cadenas y no cadenas, ha convertido las no cadenas en cadenas y las ha agregado.
El formato de cadenas proporciona una forma más poderosa de incrustar no cadenas dentro de cadenas. El formato de cadena utiliza el método de formato de una cadena para sustituir varios argumentos en la cadena.
"""
nums = [4,1,3]
formating = "Numeros :{0},{1},{2}".format(nums[0],nums[1],nums[2])
print(formating)

print()

"""
El formateo de cadenas también se puede hacer con argumentos con nombre.
"""
forvar = "Letra: {x},{y}".format(x=1, y=2)
print(forvar)
