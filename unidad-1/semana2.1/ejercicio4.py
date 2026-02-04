#pedir las tres notas

nota1 = float(input("ingrese la primera nota:"))
nota2 = float(input("ingrese la segunda nota:"))
nota3 = float(input("ingrese la tercera nota"))

# calcular el promedio 

promedio = (nota1 + nota2 + nota3) / 3 
# miostrar el resultado 

if promedio >= 60:
     print("aprovado")
else: 
     print("reprobado")