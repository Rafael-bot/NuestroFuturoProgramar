"""
Crear una calculadora

Esta lección trata sobre un proyecto de Python de ejemplo: una calculadora simple.
Cada parte explica una sección diferente del programa.
La primera sección es el menú general. Esto sigue aceptando la entrada del usuario hasta que el usuario ingresa "salir", por lo que se usa un ciclo while.

print("-----------------------------------------\nCalculadora\n-----------------------------------------")
while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
   user_input = input("Escriba la palabra: ")

    if user_input == "quit":
        break
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
       else:
           print("Intentelo otra vez")

print()
"""
"""
La siguiente parte del programa es obtener los números con los que el usuario quiere hacer algo.
El siguiente código muestra esto para la sección de suma de la calculadora. Debería escribirse un código similar para las otras secciones.

elif user_input == "add":
  num1 = float(input("Enter a number: "))
  num2 = float(input("Enter another number: "))

"""

