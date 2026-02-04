# solicitar el año 

anio = int(input("ingrese un año:"))
valor = anio % 4 

if ( valor == 0):
    print("el año es bisiesto")
else: 
    print(" el año no es bisiesto")