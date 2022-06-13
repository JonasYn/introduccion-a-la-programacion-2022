#Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
#hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
#cargar. Una vez ingresadas las notas, el programa debe informar la nota
#promedio (tenga cuidado de no incluir al -1 dentro del promedio).

nota = int(input(f"ingrese las notas de parciales o -1 para finalizar"))
while nota != "-1":
    promedio= (nota + nota + nota) / 2
    print (f" su nota es ", promedio)
    nota = int(input(f"ingrese las notas de parciales o -1 para finalizar"))
