# Conversor de tiempo 
# Pedimos al usuario la cantidad de segundos
try:
    segundos = int(input("Ingresa la cantidad de segundos: "))
    if segundos < 0:
        print("No se permiten números negativos.")
        exit()
except ValueError:
    print("Debes ingresar un número entero.")
    exit()

print("Elige la conversión:")
print("1 - A minutos")
print("2 - A horas")

try:
    opcion = int(input("Ingresa tu opción (1 o 2): "))
except ValueError:
    print("Debes ingresar un número entero.")
    exit()

match opcion:
    case 1:
        resultado = segundos / 60
        print(f"{segundos} segundos equivalen a {resultado:.2f} minutos.")
    case 2:
        resultado = segundos / 3600
        print(f"{segundos} segundos equivalen a {resultado:.2f} horas.")
    case _:
        print("Opción inválida. Debes ingresar 1 o 2.")