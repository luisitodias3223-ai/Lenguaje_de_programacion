# Piedra, Papel o Tijera 

# Valor fijo de la computadora (puedes cambiarlo para probar)
computadora = 2  # 1: Piedra, 2: Papel, 3: Tijera

# Mostrar instrucciones
print("Elige una opción:")
print("1 - Piedra")
print("2 - Papel")
print("3 - Tijera")

try:
    usuario = int(input("Ingresa tu elección (1, 2 o 3): "))
except ValueError:
    print("Debes ingresar un número.")
    exit()

match usuario:
    case 1:
        eleccion_usuario = "Piedra"
    case 2:
        eleccion_usuario = "Papel"
    case 3:
        eleccion_usuario = "Tijera"
    case _:
        print("Opción inválida")
        exit()

match computadora:
    case 1:
        eleccion_computadora = "Piedra"
    case 2:
        eleccion_computadora = "Papel"
    case 3:
        eleccion_computadora = "Tijera"

print(f"Tú elegiste: {eleccion_usuario}")
print(f"La computadora eligió: {eleccion_computadora}")

if usuario == computadora:
    print("¡Empate!")
elif (usuario == 1 and computadora == 3) or \
     (usuario == 2 and computadora == 1) or \
     (usuario == 3 and computadora == 2):
    print("¡Ganaste!")
else:
    print("¡Perdiste!")