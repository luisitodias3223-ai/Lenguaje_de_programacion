# Programa: Ángulo a punto cardinal 

# Pedimos al usuario un ángulo
try:
    angulo = int(input("Ingresa un ángulo (0, 90, 180, 270): "))
except ValueError:
    print("Debes ingresar un número entero.")
    exit()

match angulo:
    case 0:
        punto_cardinal = "Norte"
    case 90:
        punto_cardinal = "Este"
    case 180:
        punto_cardinal = "Sur"
    case 270:
        punto_cardinal = "Oeste"
    case _:
        print("Ángulo inválido. Debe ser 0, 90, 180 o 270.")
        exit()

print(f"El ángulo {angulo}° corresponde al punto cardinal: {punto_cardinal}")