num1 = float(input("ingrese el primer numero "))
num2 = float(input("ingrese el segundo numero"))

print("elige una operacion:")
print(" 1. sumar ")
print(" 2. restar ")
print(" 3. multiplicar")
print(" 4. dividir ")

opcion = int(input("ingrese una operacion ( 1-4):"))

match opcion:
    case 1:
        print("resultado:", num1 + num2)
    case 2:
        print("resultado:", num1 -num2)
    case 3:
        print("resultado:", num1 * num2)
    case 4:
        if num2 != 0:
         print("resultado:", num1 / num2)
        else:
          print("error: no se puede dividir entre cero.")
        
        print("opcion invalida ")