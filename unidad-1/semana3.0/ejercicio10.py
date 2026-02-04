saldo = 1000.0  # saldo inicial

print("Bienvenido al cajero automático")
print("Elige una opción:")
print("1. Ver saldo")
print("2. Depositar")
print("3. Retirar")

opcion = int(input("Opción (1-3): "))

match opcion:
    case 1:
        print(f"Tu saldo actual es: ${saldo:.2f}")
    case 2:
        deposito = float(input("Ingresa la cantidad a depositar: "))
        if deposito > 0:
            saldo += deposito