try:
  print(1)
  print(20 / 0)
  print(2)#Este numero no se va a imprimir
except ZeroDivisionError:
  print(3)
finally:
  print(4)

print()

open("EscribirArchivo.txt","wb")#Binario

print()

try:
    with open("AbrirArchivo.txt") as f:
        print(f.read())
except:
    print("Error")

print()

try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)

