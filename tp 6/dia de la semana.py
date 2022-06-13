# Cree un script que, dado un número de día de la semana ingresado por
# teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
# números y días de la semana es la siguiente

from re import I


def dia_semana (x):
    if x == 1:
        dia= print (f"es domigo")
    if x == 2:
        dia= print (f"es lunes")
    if x == 3:
        dia= print (f"es martes")
    if x == 4:
        dia= print (f"es miercoles")
    if x == 5:
        dia= print (f"es jueves")
    if x == 6:
        dia= print (f"es viernes")
    if x == 7:
        dia= print (f"es sabado")
    if x > 7:
        dia= print (f"pelotudo te dije un numero del 1 al 7")
    return dia
insertar_dia= int(input(f"ingrese unn numero del 1 al 7"))

dia_semana (insertar_dia)