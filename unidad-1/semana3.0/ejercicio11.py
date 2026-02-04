# Pedimos la nota al usuario
nota = int(input("Introduce una nota (1-10): "))

# Usamos match para determinar el rango
match nota:
    case 1 | 2 | 3 | 4:
        print("Insuficiente")
    case 5 | 6:
        print("Suficiente")
    case 7 | 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")
    case _:  # Para cualquier otro valor que no esté entre 1 y 10
        print("Nota inválida. Introduce un número entre 1 y 10.")