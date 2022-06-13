# Cree un script que le solicite al usuario ingresar 10 números, y una vez
# ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
# ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
# y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
# ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.

# Extienda el script del ejercicio anterior para que también informe el número
# mínimo ingresado, y su posición.



for x in range(10):
    num= int(input(f"ingrese 10 numeros{x}"))

    if x == 0:
        mayor = num
        menor = num
        posicion_mayor = x
        posicion_menor = x

    if num > mayor:
        mayor = num
        posicion_mayor = x
        
    
    if num < menor:
        menor = num 
        posicion_menor = x
        

print (f" el numero mayor es {mayor} su posicion es {posicion_mayor} , el numero menor es {menor} su posicion es {posicion_menor}")
