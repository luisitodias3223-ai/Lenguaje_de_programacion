#calculadora de descuento 
f= 0.15
p=int(input ("ingrese el precio del producto"))
if(p>=100):
    d=(p*f)
    g=p-d
    print(f"el total de tu producto es: {g}")
else:
    print("no es suficiente para su descuento")