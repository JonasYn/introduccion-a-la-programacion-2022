#Cree un script que le solicite a un alumno ingresar su apellido, la nota del
#primer parcial, y la nota del segundo parcial. Finalmente, se debe mostrar un
#reporte con la siguiente información:
#Alumno [APELLIDO]:
#- Primer parcial: [NOTA1].
# Segundo parcial: [NOTA2].
# Promedio: [PROMEDIO].

apellido = input(f"ingrese su apellido")
nota1 = int(input(f"ingrese la nota del primer parcial"))
nota2 = int(input(f"ingrese la nota del segundo parcial"))
promedio = (nota1 + nota2) / 2
print (f"alumno {apellido}")
print (f"primer parcial {nota1}")
print (f"segundo parcial {nota2}")
print (f"Promedio {promedio}")