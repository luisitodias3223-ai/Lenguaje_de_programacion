import math

numero = float(input("Ingresa un número: "))

print("Elige una operación:")
print("1. Elevar al cuadrado")
print("2. Raíz cuadrada")

opcion = int(input("Opción (1-2): "))

match opcion:
    case 1:
        resultado = numero ** 2
        print(f"El cuadrado de {numero} es {resultado}")
    case 2:
        if numero >= 0:
            resultado = math.sqrt(numero)
            print(f"La raíz cuadrada de {numero} es {resultado}")
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    