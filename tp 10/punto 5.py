# Python nos permite averiguar si determinado caracter o palabra está dentro de
# un string, mediante el uso de la palabra reservada in. La misma se utiliza de la
# siguiente manera:
# if contenido in palabra:
# # código a ejecutar si el contenido está dentro de la palabra
# Haga uso de esta funcionalidad para pedirle al usuario que ingrese una frase
# por teclado, y luego verifique si la misma contiene alguna letra ‘ñ’, y si además
# contiene la palabra ‘hola’. Informe en pantalla tanto en caso afirmativo como
# negativo.

frase = input("por favor ingrese una frase : ")
if "hola" in frase:
   print ("la palabra ingresada tiene hola ")
elif "ñ" in frase:
  print ("la palabra tiene ñ")
else:
  print ("la palabra ingresada no tiene ñ ni hola") 