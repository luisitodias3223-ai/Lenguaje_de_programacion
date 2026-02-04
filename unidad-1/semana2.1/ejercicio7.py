# solicitar temperatura en celsius 
celsius = float(input(" ingrese la temperatura en grados celsius:"))

# preguntar el tipo de conversion 
opcion = input("¿ A que unidad deas convertirla?:")

# realizar la conversion

if opcion == "f":
    fahrenheit = (celsius * 9 / 5) + 32 
    print(f"la temperatura en fahrenheit es: { fahrenheit}")
elif opcion == "k":
    kelvin = celsius + 273.15 
    print(f"la temperatura en kelvin es: {kelvin}")
else: 
    print("opcion no valida ")