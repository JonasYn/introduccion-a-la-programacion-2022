# Cree un script que determine si un triángulo es isósceles, equilátero, o
# escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
# números, correspondientes a los tres lados del triángulo.
# equilátero = todos los lados iguales
# isósceles = dos lados iguales
# escaleno = todos los lados diferentes

def triangulo(x,y,z):
    if x == y and x== z and y == z:
        tipotriangulo = print (f"es un equilatero")
    if (x == y and x!=z) or (x==z and x != y) or (y == z and x !=y):
        tipotriangulo = print (f"es un triangulo isosceles")
    if x != y and x != z and y != z:
        tipotriangulo = print (f"es un triangulo escaleno")
    return tipotriangulo

lado1 = int(input(f"ingrese el primer lado"))
lado2 = int(input(f"ingrese el segundo lado"))
lado3 = int(input(f"ingrese el tercer lado"))

triangulo (lado1,lado2,lado3)
