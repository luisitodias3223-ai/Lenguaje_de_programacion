saldo=int(input("ingrese tu saldo inicial: "))
respuesta=input("deseas realizar la compra. s/n")
mouse= 200

if(respuesta== "s"):
    if(saldo<mouse):
        print("NO LE ALCANZA")
    else:
        saldo=saldo -mouse
        print(f"compra exitosa, su vuelto es {saldo}") 
else: 
 print("vuelva prontpo")