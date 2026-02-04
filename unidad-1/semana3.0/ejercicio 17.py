# Clasificación de vehículos 

# Pedimos el número de ruedas
try:
    ruedas = int(input("Ingresa el número de ruedas (2, 4, 6, 18): "))
except ValueError:
    print("Debes ingresar un número entero.")
    exit()

match ruedas:
    case 2:
        tipo = "Motocicleta o bicicleta"
    case 4:
        tipo = "Automóvil o SUV"
    case 6:
        tipo = "Camión pequeño o bus"
    case 18:
        tipo = "Camión de carga grande"
    case _:
        print("Número de ruedas no reconocido.")
        exit()
