 numero = parseInt(prompt("Introduce un número:"))
if (numero > 0 && numero % 2 === 0) {
    alert("El número " + numero + " es positivo y también es par.");
} else {
alert("El número no cumple AMBAS condiciones (o es negativo, o es impar, o es cero).");
}