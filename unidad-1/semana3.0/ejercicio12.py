# Pedimos al usuario que seleccione un plan
plan = int(input(
    "Selecciona un plan de suscripción:\n"
    "1: Plan Básico Q.9\n"
    "2: Plan Estándar Q.15\n"
    "3: Plan Premium Q.20\n"
    "Ingresa el número de tu plan: "
))

# Usamos match para mostrar los beneficios
match plan:
    case 1:
        print("Plan Básico Q.9")
        print("- Acceso limitado a contenido")
        print("- Sin soporte prioritario")
    case 2:
        print("Plan Estándar Q.15")
        print("- Acceso completo a contenido")
        print("- Soporte por correo electrónico")
        print("- 1 dispositivo adicional")
    case 3:
        print("Plan Premium Q.20")
        print("- Acceso completo a contenido")
        print("- Soporte prioritario 24/7")
        print("- Hasta 5 dispositivos")
        print("- Contenido exclusivo")
    case _:
        print("Opción inválida. Por favor selecciona 1, 2 o 3.")