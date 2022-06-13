# Cree un script que le solicite al usuario ingresar cuál es su color favorito,
# limitando las opciones a rojo, verde, y azul. Aclaraciones:
# - Puede asumir que el usuario ingresará los strings en minúsculas.
# Opcionalmente, puede investigar el uso de las funciones upper() y lower()
# para transformar la entrada a mayúsculas o minúsculas y evitar así
# posibles errores de validación por este detalle.
# - Al validar entre un conjunto de opciones prefijadas (en lugar de hacerlo en
# un rango), es posible que no sea necesario validar el tipo del dato
# ingresado por teclado.
# - Al detectar un dato inválido, el programa debe darle las siguientes
# opciones al usuario:
# ** DATO INVÁLIDO **
# 1. Reintentar.
# 2. Salir.
# - La opción 1. Reintentar le permite al usuario reingresar el dato de manera
# indefinida, siempre mostrando las opciones ante cada intento fallido.
# - La opción 2. Salir finaliza el programa.


ingrese_su_color_favorito = (input("por favor ingrese su color favorito"))
auxiliar = 0
ancla = True

while ancla:
    if (ingrese_su_color_favorito.isalpha):
        aux = ingrese_su_color_favorito.lower()
        if aux == "rojo" or aux == "verde" or aux == "azul":
            print (f"su color favorito {ingrese_su_color_favorito} es valido. Adios")
            ancla = False
            auxiliar = "3"
        else:
            auxiliar =input("""** DATO INVÁLIDO **
 1. Reintentar.
 2. Salir.""")

    else:
         auxiliar= input("""** DATO INVÁLIDO **
 1. Reintentar.
 2. Salir.""")
    if auxiliar.isnumeric():
         if int(auxiliar) == 1:
           ingrese_su_color_favorito = input("por favor ingrese su color favorito")
         elif int(auxiliar) == 2:
           ancla = False
         
