numero = int(input("ingrese un numero"))

match numero:
    case 1: 
        print(" hoy es Lunes")
    case 2:
        print(" hoy es Martes")
    case 3:
        print(" hoy es Miercoles")
    case 4:
        print(" hoy es Jueves")
    case 5:
        print(" hoy es Viernes") 
    case 6:
        print(" hoy es sabado")
    case 7:
        print(" hoy es Domingo")  
    case _:
        print("Numero invalido ") 