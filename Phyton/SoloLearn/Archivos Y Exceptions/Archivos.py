"""
Abrir Archivo

Puede usar Python para leer y escribir el contenido de los archivos.
Los archivos de texto son los más fáciles de manipular. Antes de poder editar un archivo, debe abrirlo con la función de abrir.
"""
print("-----------------------------------------\nAbrir Archivo\n-----------------------------------------")
try:
    archivo = open('AbrirArchivo.txt')

except FileNotFoundError:
    print("Error, no se ha encontrado el archivo")

print()

"""
Puede especificar el modo utilizado para abrir un archivo aplicando un segundo argumento a la función abierta.
Enviar "r" significa abrir en modo de lectura, que es el valor predeterminado.
Enviar "w" significa modo de escritura, para reescribir el contenido de un archivo.
Enviar "a" significa modo de adición, para agregar contenido nuevo al final del archivo.
Agregar "b" a un modo lo abre en modo binario, que se usa para archivos que no son de texto (como archivos de imagen y sonido).

"""
print("-----------------------------------------\nModos de Abrir Archivos\n-----------------------------------------")
# Modo Escrito
e = open("AbrirArchivo.txt", mode='w')

# Modo Lectura
l = open("AbrirArchivo.txt", mode='r')

# Modo Adición
a = open("AbrirArchivo.txt", mode='a')

# Modo Binariol
b = open("AbrirArchivo.txt", mode='wb')

print()

"""
Una vez que un archivo se ha abierto y utilizado, debe cerrarlo.
Esto se hace con el método de cierre del objeto de archivo.
"""
print("-----------------------------------------\nClose\n-----------------------------------------")
file = open("AbrirArchivo.txt", "w")
file.close()

print()
print()

"""
Leer Archivos

El contenido de un archivo que se ha abierto en modo texto puede leerse utilizando el método de lectura.

Para leer solo una cierta cantidad de un archivo, puede proporcionar un número como argumento para la función de lectura. Esto determina el número de bytes que se deben leer.
Puede realizar más llamadas para leer en el mismo objeto de archivo para leer más del archivo byte a byte. Sin argumento, leer devuelve el resto del archivo.

Después de que se haya leído todo el contenido de un archivo, cualquier intento de leer más de ese archivo devolverá una cadena vacía, porque está intentando leer desde el final del archivo.
"""
print("-----------------------------------------\nLeer Archivos\n-----------------------------------------")
lect = open("AbrirArchivo.txt",mode="r")
print(lect.read(5)) # Lee lo equivalenete a 5 bit
print(lect.read())  # Lee todo ya que no tiene argumentos
lect.close()

print()

"""
Para recuperar cada línea en un archivo, puede usar el método readlines para devolver una lista en la que cada elemento es una línea en el archivo.
"""
print("-----------------------------------------\nReadLines\n-----------------------------------------")
rl = open("AbrirArchivo.txt",mode="r")
print(rl.readlines())
rl.close()

print()

"""
Escribir archivos

Para escribir en archivos, utiliza el método de escritura, que escribe una cadena en el archivo.
"""
print("-----------------------------------------\nEscribir Archivo\n-----------------------------------------")
escbribir = open("EscribirArchivo.txt", "w")
escbribir.write(input("introduce el texto: "))
escbribir.close()

mostrar = open("EscribirArchivo.txt", "r")
print(mostrar.read())
mostrar.close()

print()

"""
Cuando se abre un archivo en modo de escritura, se elimina el contenido existente del archivo.
"""
lect = open("EscribirArchivo.txt", "r")
print("Reading initial contents")
print(lect.read())
print("Finished")
lect.close()

escrib = open("EscribirArchivo.txt", "w")
escrib.write(input("introduce el texto: "))
escrib.close()

most = open("EscribirArchivo.txt", "r")
print("Reading new contents")
print(most.read())
print("Finished")
most.close()

print()

"""
El método de escritura devuelve el número de bytes escritos en un archivo, si tiene éxito.
"""
msg = input("Introduce texto: ")
bite = open("EscribirArchivo.txt", "w")
amount_written = bite.write(msg)
print(amount_written)
bite.close()

print()

"""
Trabajando con archivos

Es una buena práctica evitar el desperdicio de recursos asegurándose de que los archivos siempre estén cerrados después de haber sido utilizados. Una forma de hacerlo es usar try y finalmente.
"""
print("-----------------------------------------\nTrabajar con Archivos\n-----------------------------------------")
try:
   f = open("EscribirArchivo.txt")
   print(f.read())
finally:
   f.close()

print()

"""
Una forma alternativa de hacerlo es usar declaraciones. Esto crea una variable temporal (a menudo llamada f), a la que solo se puede acceder en el bloque sangrado de la instrucción with.

El archivo se cierra automáticamente al final de la declaración with, incluso si se producen excepciones dentro de él.

"""
with open("EscribirArchivo.txt") as f:
    print(f.read())