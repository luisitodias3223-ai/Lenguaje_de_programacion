mes = int(input(" ingrese el numero del mes "))

match mes:
    case 1|3|5|7|8|10|12:
        print("este mes tiene 31 dias")
    case 4|6|9|11:
        print("este mes tiene 30 dias")
    case 2:
        print("este mes tiene 28 dias ")
    case _:
        print(" este numero es incorrecto")

