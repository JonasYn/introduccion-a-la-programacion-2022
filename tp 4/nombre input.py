#Cree un script que, al ejecutarlo, le solicite al usuario ingresar su nombre de
#pila, luego lo salude y calcule la cantidad de letras del nombre, mostrando el
#mensaje “Hola, [NOMBRE], tu nombre tiene [N] letras.”.

nombre = input (f"ingrese su nombre de pila")
cantidad_de_letras = len (nombre)  
print (f"Hola, {nombre}, tu nombre tiene {cantidad_de_letras} letras")