numero= int(input("ingrese un numero romano "))

match numero:
    case 1:
        print("I")
    case 2:
        print("II")
    case 3:
        print("III")
    case 4:
        print("IV")
    case 5:
        print("V")
    case 6:
        print("VI")
    case 7:
        print("VII")
    case 8:
        print("VIII")
    case 9:
        print("IX")
    case 10:
        print("X")
    case _:
        print("numero romano incorrecto ")