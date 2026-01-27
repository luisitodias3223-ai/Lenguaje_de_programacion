# Solicitar al Usuario su nombre y mostrarlo en
# pantalla

nom = input("Por favor escribe tu nombre: ")
print(f"Mucho gusto amigo {nom}")

"""
SOLICITAR AL USUARIO SU EDAD Y DETERMINAR SU AÑO DE 
NACIMIENTO
"""
año = 2026
edad = int(input("¿Que edad tienes? "))
nacimiento = año - edad
print(f"naciste en el año {nacimiento}")

"""
SOLICITAR AL USUARIO SU EDAD Y DETERMINAR Si es mayor 
de edad o menor, si tiene exactamente la mayoria de 
edad, decirle: ya es hora de sacar DPI
"""
edad = int(input("¿Cuantos años tienes?"))
if(edad<= 17):
    print("sigues siendo menor de edad")
else:
    print("bueno , YA ES HORA DE SACAR DPI :( )")

