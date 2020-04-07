i = 3
while i>=0:
   print(i)
   i = i - 1

print()

"""
Break
"""
i = 0
while 1==1:
  print(i)
  i += 1
  if i >= 5:
    print("Breaking")
    break

print()

"""
Continue
"""
i = 0
while True:
   i = i +1
   if i == 2:
      print("Skipping 2")
      continue
   if i == 5:
      print("Breaking 5")
      break

print()

"""
Bucles con While

A veces, debe realizar un código en cada elemento de una lista. Esto se llama iteración, y se puede lograr con un ciclo while y una variable de contador.
"""
print("-----------------------------------------\nBucles Con While\n-----------------------------------------")
words = ["hello", "world", "spam", "eggs"]
counter = 0
max_index = len(words) - 1

while counter <= max_index:
   word = words[counter]
   print(word + "!")
   counter += 1

print()

"""
Bucles con For

La iteración a través de una lista utilizando un ciclo while requiere bastante código, por lo que Python proporciona el ciclo for como un acceso directo que logra lo mismo.
"""
print("-----------------------------------------\nBucles Con For\n-----------------------------------------")
words = ["hello", "world", "spam"]
for word in words:
  print(word + "!")

print()

"""
El bucle for se usa comúnmente para repetir algún código un cierto número de veces. Esto se hace combinando bucles con objetos de rango.
"""
print("-----------------------------------------\nBucles Con For(Repetir)\n-----------------------------------------")
for i in range(5):
  print("hello!")


for i in range(0,20,2):
  print(i)

print()

