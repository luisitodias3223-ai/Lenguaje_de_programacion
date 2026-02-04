# Pedimos el salario al usuario
salario = float(input("Ingresa tu salario: Q"))

# Mostramos opciones de tipo de empleado
print("Selecciona el tipo de empleado:")
print("1: Público (10% de impuesto)")
print("2: Privado (15% de impuesto)")
print("3: Independiente (8% de impuesto)")

tipo = int(input("Ingresa el número de la opción: "))

# Calculamos el impuesto 
match tipo:
    case 1:
        impuesto = salario * 0.10
        print(f"Empleado Público: impuesto = Q{impuesto:.2f}")
        print(f"Salario después de impuesto = Q{salario - impuesto:.2f}")
    case 2:
        impuesto = salario * 0.15
        print(f"Empleado Privado: impuesto = Q{impuesto:.2f}")
        print(f"Salario después de impuesto = Q{salario - impuesto:.2f}")
    case 3:
        impuesto = salario * 0.08
        print(f"Empleado Independiente: impuesto = Q{impuesto:.2f}")
        print(f"Salario después de impuesto = Q{salario - impuesto:.2f}")
    case _:
        print("Opción inválida. Por favor selecciona 1, 2 o 3.")