# Construya un menú que le muestre al usuario lo siguiente:
# ********* MI PROGRAMA *********
# 1. Saludar.
# 2. Informar temperatura.
# 3. Mostrar nombre de materia.
# 4. Salir.
# Seleccione una opción [1-4]:
# ● - Cuando el usuario ingrese la opción 1, se mostrará el mensaje:
# “Hola, bienvenido a mi programa interactivo!”.
# ● - Cuando el usuario ingrese la opción 2, se mostrará el mensaje
# “Hay una sensación térmica de 20 grados Celsius.”.
# ● - Cuando el usuario ingrese la opción 3, se mostrará el mensaje
# “Estás en la materia Introducción a la Programación!”.
# ● - Cuando el usuario ingrese la opción 4, el programa debe terminar,
# mostrando el mensaje “Hasta la próxima!”.
# ● - Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
# inválida.”.

import os

def menu ():
  print  (f"********* MI PROGRAMA *********")
  print  (f"1. Saludar")
  print  (f"2. Informar temperatura")
  print  (f"3. Mostrar el nombre de la materia")
  print  (f"4. Salir")



programa = ""


while programa != 4:
    os.system("cls")
    menu()
    
    programa =int(input(f"ingrese una de las anteriores opciones"))

    if programa == 1:
        print (f"Hola, bienvenido a mi programa interactivo!")
    elif programa == 2:
        print (f"Hay una sensación térmica de 20 grados Celsius.")
    elif programa == 3:
        print (f"Estás en la materia Introducción a la Programación!")
    elif programa == 4:
        print (f"Hasta la próxima!" ) , 
           
    else:
        print (f"opcion invalida")

        
    input(f"PRESIONE ENTER PARA CONTINUAR")