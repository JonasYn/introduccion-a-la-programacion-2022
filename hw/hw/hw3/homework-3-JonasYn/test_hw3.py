# IMPORTANTE: No modificar ni borrar este archivo
from hw3 import sumatoria, factorial, sumaParesOImpares, sumaEspaciadaDel1al100, teLoRepitoNVeces

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