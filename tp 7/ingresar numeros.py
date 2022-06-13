# Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada
# uno, informarle si el mismo es positivo, negativo, o cero.

for signo in range (10):
    ingresar= int(input(f"ingrese 10 numeros: "))

    if ingresar > 0:
        print (f"es positivo")

    if ingresar < 0:
         print (f"el signo es negativo")
    
    if ingresar == 0:
        print (f"el numero es 0")

    


