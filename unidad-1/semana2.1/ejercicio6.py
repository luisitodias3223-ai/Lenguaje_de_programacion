# solicitar datos al usuario 

dividiendo = float(input("ingrese el dividiendo:"))
divisor = float(input(" ingrese el divisor:"))

# verificar que le divisor no sea cero 

if divisor != 0: 
     resultado = dividiendo / divisor
     print(f" el resultado de la divisoon es: {resultado}")
else: 
      print ("error: no se puede dividir")