#comparador de numeros 

num1=float(input("ingrese el primer numero"))
num2=float(input("ingrese el segundo numero"))

if num1 > num2:
    print(f"El numero mayor es: {num1}")
elif num2 > num1:
    print(f"el numero mayor es: {num2}")
else:
    print("Ambos numeros son iguales")