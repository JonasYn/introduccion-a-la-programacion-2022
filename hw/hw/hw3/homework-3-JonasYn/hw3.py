################################################################################################
# Nombre de archivo: hw3.py (No cambiar el nombre de este archivo)
# El repositorio donde esta tu HW3 es: github.com/unlu-edu-ar/homework-3-TuNombreDeUsuarioGithub
#
# Completa con tu nombre, apellido y DNI
# Nombre y Apellido: jonas ynsaurralde
# DNI: 44378573
################################################################################################


#################################################
# Funciones que tenés que programar
#################################################

# Cree una función que recibe dos números enteros positivos n1 y n2 como 
# parámetros, donde n1 < n2, y retorna el resultado de sumar los números enteros 
# contenidos en el intervalo [n1...n2]
def sumatoria(n1, n2):
    resultado = 0
    for i in range (n1, n2+1):
        resultado += i
    return resultado
    

# Cree una función que recibe un número entero n mayor o igual a cero como 
# parámetro, y retorna el factorial de dicho número. Recuerde que el factorial 
# de 0 es 0!=1, el factorial de 1 es 1!=1, y el factorial de n = n! = 
# 1 * 2 * 3 * … * (n - 1) * n
def factorial(n):
    resultado = 1
    for i in range (1,n+1):
        resultado = resultado * i
    return resultado

# Cree una función que recibe como parámetros dos números enteros positivos n1 y 
# n2, donde n1 < n2, y un booleano. Si el booleano fuese True, la función retorna 
# el resultado de sumar los números enteros pares contenidos en el intervalo 
# [n1...n2]. Si el booleano fuese False, la función retorna el resultado de sumar 
# los números enteros impares contenidos en el intervalo [n1...n2].
def sumaParesOImpares(n1, n2, pares):
    var1= 0
    if pares == True:
        for i in range (n1 , n2+1):
            if i % 2 == 0:
                var1 += i
            resultado = var1
    elif pares == False:
        for i in range (n1, n2+1):
            if i % 2 == 1:
                var1 += i
            resultado = var1
    return resultado
 
# Cree una función que recibe como parámetro un número entero n, donde 0 <= n < 100, 
# y retorna la sumatoria de los números enteros contenidos en el intervalo [1...100], 
# espaciados por n números.
def sumaEspaciadaDel1al100(n):
    suma = 0
    for i in range (1,101,n+1):
        suma += i
    return suma



# Cree una función que recibe como parámetros un string y un número entero 
# positivo n, y retorna el string pasado como parámetro concatenado n veces.
def teLoRepitoNVeces(mensaje, n):
    resultado = mensaje * n
    return resultado
    

#################################################
# Funciones de Test (no modificar)
#################################################

def testSumatoria():
    print('Testeando testSumatoria()... ', end='')
    assert sumatoria(1, 3) == 6 
    assert sumatoria(5, 6) == 11
    assert sumatoria(3, 7) == 25
    print('Pasó!')

def testFactorial():
    print('Testeando testFactorial()... ', end='')
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(5) == 120
    print('Pasó!')

def testSumaParesOImpares():
    print('Testeando testSumaParesOImpares()... ', end='')
    assert sumaParesOImpares(1, 5, True) == 6
    assert sumaParesOImpares(1, 5, False) == 9
    assert sumaParesOImpares(10, 20, True) == 90
    assert sumaParesOImpares(11, 12, False) == 11    
    print('Pasó!')

def testSumaEspaciadaDel1al100():
    print('Testeando testSumaEspaciadaDel1al100()... ', end='')
    assert sumaEspaciadaDel1al100(0) == 5050
    assert sumaEspaciadaDel1al100(99) == 1
    assert sumaEspaciadaDel1al100(9) == 460 
    print('Pasó!')

def testTeLoRepitoNVeces():
    print(' Testeando testTeLoRepitoNVeces()... ', end='')
    assert teLoRepitoNVeces('Hello world', 1) == 'Hello world'
    assert teLoRepitoNVeces('CambioDolar', 3) == 'CambioDolarCambioDolarCambioDolar'
    assert teLoRepitoNVeces('Hola mundo! ', 4) == 'Hola mundo! Hola mundo! Hola mundo! Hola mundo! '
    print('Pasó!')

#################################################
# testearTodo y main
#################################################

def testearTodo():
    # comentá los tests que no querés correr!
    testSumatoria()
    testFactorial()
    testSumaParesOImpares()
    testSumaEspaciadaDel1al100()
    testTeLoRepitoNVeces()

def main():
    testearTodo()

if __name__ == '__main__':
    main()
