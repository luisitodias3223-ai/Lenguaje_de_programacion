 entrada = prompt("Ingresa un número:")
 numero = parseFloat(entrada)

if (numero > 0) {
    alert("El número " + numero + " es positivo.")
    alert("Es positivo")
} else if (numero === 0) {
    alert("El número es cero.")
} else {
    alert("El número no es positivo (es negativo).")
}
