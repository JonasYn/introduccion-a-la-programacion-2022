# Como su nombre lo indica, los strings son cadenas de caracteres, es decir, una
# sucesión de símbolos. Si lo entendemos de esta manera, podemos utilizar una
# estructura iterativa, por ejemplo el for, para recorrer uno a uno los caracteres de
# un string, de la siguiente manera:
# for letra in un_string:
# # código por cada caracter
# Haga uso de esto para implementar un script que le solicite al usuario ingresar
# su nombre, y luego imprima cada una de las letras en un renglón diferente de
# la terminal.

nombre = input("ingrese su nombre")
for i in len(nombre) :
    print (i)