# estacion del año 

mes  = int(input("ingrese el numero del mes (1-12):"))

match mes:
    case 12| 1 | 2:
        print("invierno")
    case 3|4|5:
        print("primavera")
    case 6|7|8:
        print("verano")
    case 9|10|11:
        print("otoño")
    case _:
     print("numero incorrecto")
