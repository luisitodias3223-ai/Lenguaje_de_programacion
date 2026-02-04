print("Ingresa la temperatura en Celsius:")
celsius = float(input())

print("Elige a qué convertir:")
print("1. Fahrenheit")
print("2. Kelvin")

opcion = int(input("Opción (1-2): "))

match opcion:
    case 1:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C son {fahrenheit}°F")
    case 2:
        kelvin = celsius + 273.15
        print(f"{celsius}°C son {kelvin} K")
    case _:
        print("Opción inválida.")