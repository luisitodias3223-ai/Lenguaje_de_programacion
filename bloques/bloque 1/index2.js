respuesta = prompt("Ingresa un número para saber si es negativo:")
 numero = parseFloat(respuesta)

if (numero < 0) {
    alert("El número " + numero + " es negativo.")
    alert("Resultado: Negativo")
} else if (numero > 0) {
    alert("El número es positivo.")
    alert("Resultado: Positivo")
} else if (numero === 0) {
    alert("El número es cero (neutro).")
    alert("Resultado: Neutro")
} else {
    alert("Eso no parece ser un número válido.")
}
