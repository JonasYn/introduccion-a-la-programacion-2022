# IMPORTANTE: No modificar ni borrar este archivo
from hw5 import extraePares,productoriaYSumatoria,sumaSubcadena

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
