"""
Analizador de texto

Este es un proyecto de ejemplo, que muestra un programa que analiza un archivo de muestra para encontrar qué porcentaje del texto ocupa cada personaje.
Esta sección muestra cómo se puede abrir y leer un archivo.
"""
try:
    filename = input("Introduzca el nombre del archivo: ")#Tenemos que introducir la ruta del archivo
    with open(filename) as f:
        text = f.read()
    print(text)
except FileNotFoundError:
    print("No se ha encontrado el archivo")

print()


try:
    """
    Esta parte del programa muestra una función que cuenta cuántas veces se produce un carácter en una cadena.
    """
    def contcaracter(text, char):
        cont = 0
        for c in text:
            if c == char:
                cont += 1
        return cont

    filename = input("Introduzca el nombre del archivo: ")  # Tenemos que introducir la ruta del archivo
    with open(filename) as f:
        text = f.read()

    print(text)
    caracter = "e"
    """
    Esta función toma como argumentos el texto del archivo y un carácter, devolviendo el número de veces que ese carácter aparece en el texto.
    Ahora podemos llamarlo para nuestro archivo.
    """
    print("La letra ",caracter," se repite ",contcaracter(text,caracter),".")

except FileNotFoundError:
    print("No se ha encontrado el Archivo")

print()


def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

"""
La siguiente parte del programa encuentra qué porcentaje del texto ocupa cada carácter del alfabeto.
"""


