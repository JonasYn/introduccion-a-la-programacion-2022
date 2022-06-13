ancla = True
contador = 1
ingresar_edad = input("ingrese su edad entre 18 y 60 años: ")
while ancla:

    contador += 1
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
    if contador == 10:
        print ("“Usted está jugando conmigo, yo me retiro”.")
        ancla = False