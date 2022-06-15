################################################################################################
# Nombre de archivo: hw5.py (No cambiar el nombre de este archivo)
# El repositorio donde esta tu HW5 es: github.com/unlu-edu-ar/homework-5-TuNombreDeUsuarioGithub
#
# Completa con tu nombre, apellido y DNI
# Nombre y Apellido: Jonas Ynsaurralde
# DNI: 44.378.573
################################################################################################


#################################################
# Funciones que tenés que programar
#################################################

# Cree una función que recibe una lista l de números enteros y retorna una lista
# de los números pares de la lista l, conservando el orden que tenían dichos
# números pares en la lista l. Si no hay ningún número par en la lista l, deberá
# retornar una lista vacía.
# Ejemplo, si l=[1,0,-4,-5,2,0] deberá retornar la lista [0,-4,2,0]
from audioop import mul


def extraePares(l):
    lista_de_pares = []
    for i in range (len(l)):
        if l[i] % 2 == 0:
            lista_de_pares.append(l[i])
    return lista_de_pares

# Cree una función que recibe una lista no vacía l de números enteros y retorna 
# un entero m con la multiplicación de todos los números de la lista, y un número 
# entero s con la sumatoria de los elementos de la lista l.
# Ejemplo: l=[-1,2,3] debe retornar (-6,4)
# Ejemplo: l=[-1,0,3] debe retornar (0,2)
def productoriaYSumatoria(l):
    suma = 0
    multiplicacion = 1
    for i in range (len(l)):
        multiplicacion *= l[i]
        suma += l[i]
    return multiplicacion, suma


# Cree una función que recibe como parámetros una lista l no vacía de números 
# enteros, dos números enteros naturales n1 y n2, donde 0<=n1<=n2<len(l), y 
# un booleano. Si el booleano fuese True, la función retorna 
# el resultado de sumar los números enteros pares contenidos en el intervalo 
# l[n1...n2] (si no hay ningún número par en el intervalo retorna 0). Si el 
# booleano fuese False, la función retorna el resultado de sumar los números 
# enteros impares contenidos en el intervalo l[n1...n2] (si no hay ningún número 
# impar en el intervalo retorna 0).
def sumaSubcadena(l, n1, n2, pares):
    numeros_enteros= 0
    if pares:
        for i in range (len(l)):
            if i >= n1 and i <= n2:
                if l[i] % 2 == 0:
                    numeros_enteros += l[i]
    else:
        for i in range (len(l)):
            if i >= n1 and i <= n2:
                if l[i] % 2 != 0:
                    numeros_enteros += l[i]
    return numeros_enteros


#################################################
# Funciones de Test (no modificar)
#################################################

def testExtraePares():
    print('Testeando extraePares()... ', end='')
    assert extraePares([1,0,-4,-5,2,0])==[0,-4,2,0]
    assert extraePares([])==[]
    assert extraePares([0])==[0]
    assert extraePares([3,1])==[]
    assert extraePares([2,4,2])==[2,4,2]
    print('Pasó!')

def testProductoriaYSumatoria():
    print('Testeando productoriaYSumatoria()... ', end='')
    assert productoriaYSumatoria([-1,2,3])==(-6,4)
    assert productoriaYSumatoria([-1,0,3])==(0,2)
    assert productoriaYSumatoria([0])==(0,0) 
    assert productoriaYSumatoria([2])==(2,2)   
    print('Pasó!')

def testSumaSubcadena():
    print('Testeando sumaSubcadena()... ', end='')
    assert sumaSubcadena([1,2,3],0,1,True)==2
    assert sumaSubcadena([1,2,3],2,2,False)==3  
    assert sumaSubcadena([1,2,2],2,2,False)==0  
    assert sumaSubcadena([0],0,0,True)==0   
    assert sumaSubcadena([1],0,0,False)==1 
    assert sumaSubcadena([1,2,3,4],1,3,True)==6
    print('Pasó!')

#################################################
# testearTodo y main
#################################################

def testearTodo():
    # comentá los tests que no querés correr!
    testExtraePares()
    testProductoriaYSumatoria()
    testSumaSubcadena()

def main():
    testearTodo()

if __name__ == '__main__':
    main()
