#calculadora de IMC 

peso = float(input("ingrese tu peso en kg:"))
altura = float(input("ingrese tu altura en metros:"))

imc = peso / (altura ** 2)
print(f" tu imc es: {imc:.2f}")

if imc> 25:
 print ("HAY SOBREPESO.")
else:
 print("NO HAY SOBREPESO")