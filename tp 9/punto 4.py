# La técnica de validación para un conjunto específico de valores se puede utilizar
# para construir menús de opciones. Construya un menú que le muestre al
# usuario lo siguiente:
# ********* MI PROGRAMA *********
# 1. Saludar.
# 2. Informar temperatura.
# 3. Mostrar nombre de materia.
# 4. Salir.
# Seleccione una opción [1-4]:
# - Cuando el usuario ingrese la opción 1, se mostrará el mensaje “Hola,
# bienvenido a mi programa interactivo!”.
# - Cuando el usuario ingrese la opción 2, se mostrará el mensaje “Hay una
# sensación térmica de 20 grados Celsius.”.
# - Cuando el usuario ingrese la opción 3, se mostrará el mensaje “Estás en la
# materia Introducción a la Programación!”.
# - Cuando el usuario ingrese la opción 4, el programa debe terminar,
# mostrando el mensaje “Hasta la próxima!”.
# - Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
# inválida.”.
print ("""********* MI PROGRAMA *********
# 1. Saludar.
# 2. Informar temperatura.
# 3. Mostrar nombre de materia.
# 4. Salir""")

ancla = True
ingresar_opcion = input("por favor ingrese una de las opcione")

while ancla:
    import os
    os.system('cls')
    print ("""********* MI PROGRAMA *********
     # 1. Saludar.
     # 2. Informar temperatura.
     # 3. Mostrar nombre de materia.
     # 4. Salir""")
     
    if ingresar_opcion.isnumeric():
        if int(ingresar_opcion) >= 1 and int(ingresar_opcion) <= 4:
            if int(ingresar_opcion) == 1:
                print ("Hola, bienvenido a mi programa interactivo!")
                ingresar_opcion = input("porfavor ingrese otra opcion o 4 para salir")
            elif int(ingresar_opcion) == 2:
                print ("Hay una sensación térmica de 20 grados Celsius.")
                ingresar_opcion = input("porfavor ingrese otra opcion o 4 para salir")
            elif int(ingresar_opcion) == 3:
                print ("Estás en la materia Introducción a la Programación!")
                ingresar_opcion = input("porfavor ingrese otra opcion o 4 para salir")
            elif int(ingresar_opcion) == 4:
                os.system("cls")
                print ("Hasta la próxima")
                ancla = False
        else:
            ingresar_opcion = input(f"el dato {ingresar_opcion} no es valido, por favor reintentelo")
    else:
         ingresar_opcion = input(f"el dato {ingresar_opcion} no es valido, por favor reintentelo")