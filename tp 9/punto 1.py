# Cree un script que le solicite al usuario ingresar una temperatura en grados
# Celsius, y valide que la entrada es correcta, teniendo en cuenta que la
# temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El
# programa debe permitir reingresar el dato cuantas veces sea necesario, hasta
# que el usuario provea un dato válido. Procure informar al usuario cuando su
# dato es inválido, y cuáles son los valores aceptados.


ancla = True
ingresar_temperatura = input(f"ingrese la temperatura en celsius entre -18 y 50: ")
while ancla:
    if ingresar_temperatura.isalpha():
         ingresar_temperatura = input(f"El dato {ingresar_temperatura} no es valido, reintentelo: ")
    elif ingresar_temperatura.isnumeric():
        if int(ingresar_temperatura) > -18 and int(ingresar_temperatura)< 50:
             print (f"el dato {ingresar_temperatura} es valido. Adios")
             ancla = False
        else:
            ingresar_temperatura = input(f"El dato {ingresar_temperatura} no es valido, reintentelo: ")
    else:
        ingresar_temperatura = input(f"El dato {ingresar_temperatura} no es valido, reintentelo: ")
        