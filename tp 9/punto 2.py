# Cree un script que le solicite al usuario ingresar su edad. Verifique que el dato
# ingresado sea válido, teniendo en cuenta que la edad es un número entero, y el
# rango válido para este programa es de 18 a 60 años. El programa debe solicitar
# el reingreso de manera indefinida, hasta que el dato sea correcto.
import os
ancla = True
ingresar_edad = input("ingrese su edad entre 18 y 60 años: ")
while ancla:
    os.system('cls')
    if ingresar_edad.isalpha():
         ingresar_edad = input(f"El dato {ingresar_edad} no es valido, reintentelo: ")
    elif ingresar_edad.isnumeric():
        if int(ingresar_edad) > 18 and int(ingresar_edad)< 60:
             print (f"el dato {ingresar_edad} es valido. Adios")
             ancla = False
        else:
            ingresar_edad = input(f"El dato {ingresar_edad} no es valido, reintentelo: ")
    else:
        ingresar_edad= input(f"El dato {ingresar_edad} no es valido, reintentelo: ")