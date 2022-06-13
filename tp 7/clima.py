# Un cliente ha solicitado un programa que le permita ingresar los mililitros de
# lluvia caídos diariamente en una semana, para que el programa le informe en
# pantalla el promedio de precipitación de esa semana. El cliente también desea
# saber cuál fue el día en que más llovió en la semana.
# A modo ilustrativo, un reporte generado por el programa debería verse como
# sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
# El promedio de precipitaciones fue de XX mls. diarios.
# El día de más precipitaciones fue el xxxxxx (nombre del día).
# Tenga en cuenta que la numeración de los días de la semana comienza con el 1
# para el día domingo.
# Codifique el programa para dar solución a lo solicitado por el cliente.

suma = 0
contador = 0
promedio = 0
dia_que_mas_llovio = 0
dia_max = 0
for dia in range(1,8):
   mm= float(input(f"ingrese los mililitros que llovio {dia }"))
   suma += mm
   contador += 1
   if mm > dia_que_mas_llovio:
       dia_que_mas_llovio = mm
       dia_max = dia
#  if mm > dia_que_mas_llovio:
#     dia_que_mas_llovio = mm
#     dia_max = contador

promedio = suma / contador


print (f"en total llovio {suma} y el promedio es {promedio} y el dia que mas precipitado fue {dia_max}")