# Cree un script que le solicite a un alumno de la asignatura Introducción a la
# Programación que ingrese las notas de sus dos parciales. Como resultado, se
# le debe informar al alumno su situación, junto con la nota promedio. Las
# reglas para saber la situación de un alumno son las siguientes:

def promedio(x,y):
    nota = (x+y) / 2
    if nota >= 8:
        situacion = print (f"promovido")
    if nota <8 and nota >= 4:
        situacion = print (f"regular")
    if nota < 4:
        situacion = print (f"libre")
    return situacion
 
nota1 = int(input(f"ingrese la nota de su primer parcial"))
nota2 = int(input(f"ingrese la nota de su segundo parcial"))

promedio (nota1,nota2)