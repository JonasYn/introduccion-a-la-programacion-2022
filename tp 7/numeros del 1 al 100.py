# Cree un script para mostrar los primeros 100 números enteros positivos,
# comenzando desde el 1.

#for menganito in range(1, 101):
 #   print (menganito)


#parte 2 Modifique el script del ejercicio anterior para que se muestren sólo los números
#pares. Para saber si un número es par, utilice el operador de módulo (%).

for menganito in range(1, 101):
    pares = menganito % 2
    if pares == 0:
        print (menganito)