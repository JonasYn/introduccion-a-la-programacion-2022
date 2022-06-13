# Cree un script que le solicite al usuario ingresar un número entero, y muestre
# en pantalla el factorial de dicho número. NOTA: puede obviar la validación en
# este ejercicio, pero recuerde que la función range no incluye al valor máximo
# enviado como parámetro.
# factorial de n = n! = 1 * 2 * 3 * ... * (n - 1) * n




num1 = int(input(f"ingrese el numero que quiera obtener el factorial: "))

factorial = 1

for i in range(1,num1+1):
    factorial = factorial * i

print (f"el factorial de su numero es {factorial}")