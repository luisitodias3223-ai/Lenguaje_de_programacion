import math

print(" elige una figura para calcular su area:")
print(" 1. cuadrado")
print(" 2. triangulo")
print("  3. circulo")

opcion = int(input("ingresa tu opcion (1-3)"))

match opcion:
    case 1: 
        lado = float(input("ingrese el lado del cuadrado"))
        area = lado ** 2
        print(" el area del cuadrado es:, area ")
    case 2: 
        base  = float(input("ingrese la base  del triangulo"))
        altura  = float(input(" ingrese la altura del triangulo:"))
        area = ( base * altura) / 2 
        print ("el area del triangulo es", area)
    case 3: 
        radio = float(input("ingrese el radio del circulo"))
        area = math.pi * radio ** 2 
        print(" el area del circulo es:", area )

        
        print("opcion incorrecta ")