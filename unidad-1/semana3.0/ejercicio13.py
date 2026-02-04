# Pedimos la cantidad en moneda local
cantidad = float(input("Ingresa la cantidad en Q: "))

# Mostramos opciones de conversión
print("Elige la divisa a la que deseas convertir:")
print("1: Dólares")
print("2: Euros")
print("3: Libras")

opcion = int(input("Ingresa el número de la opción: "))

# Tasas de ejemplo (puedes actualizarlas según el valor real)
tasa_dolar = 7.8   # 1 USD = 7.8 Q
tasa_euro = 8.5    # 1 EUR = 8.5 Q
tasa_libra = 9.5   # 1 GBP = 9.5 Q

# Conversión usando match
match opcion:
    case 1:
        conversion = cantidad / tasa_dolar
        print(f"{cantidad} Q equivalen a {conversion:.2f} USD")
    case 2:
        conversion = cantidad / tasa_euro
        print(f"{cantidad} Q equivalen a {conversion:.2f} EUR")
    case 3:
        conversion = cantidad / tasa_libra
        print(f"{cantidad}  Q equivalente a {conversion:.2f} GBP")
        
        print("opcion invalida")
              