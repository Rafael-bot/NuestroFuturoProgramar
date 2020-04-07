"""
Finally

Para garantizar que se ejecute algún código sin importar qué errores ocurran, puede usar una declaración de finalización. La última declaración se coloca en la parte inferior de una declaración de prueba / excepción. El código dentro de una declaración de finalización siempre se ejecuta después de la ejecución del código en los bloques try y posiblemente.
"""
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("Fin")