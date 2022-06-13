#Codifique un programa que le solicite al usuario ingresar números enteros,
#y que vaya mostrando el resultado de multiplicar por 2 cada uno.
#El programa debe terminar cuando el usuario ingresa el valor especial -1.



numeros_enteros = input(f"ingrese numeros enteros o ingrese -1 para finalizar")
while numeros_enteros != "-1":
    resultado = int(numeros_enteros) * 2 
    print (resultado)
    numeros_enteros = input(f"ingrese numeros enteros o ingrese -1 para finalizar")
