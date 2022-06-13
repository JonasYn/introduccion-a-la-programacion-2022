#Cree un script que le solicite al usuario ingresar un número por teclado, y le
#informe con un mensaje si su número es positivo, negativo, o 0.

def positivo_negativo(x):
     if x < 0:
         numero = print (f"su numero es negativo")
     elif x > 0:
         numero = print(f"su numero es positivo")
     elif x == 0:
         numero = print (f"su numero es igual a 0")
     return numero
numero1= int(input(f"inghrese un numero"))
positivo_negativo (numero1)