 numero = parseFloat(prompt("Introduce un número:"))
if (numero < 0 || numero > 100) {
    alert("El número " + numero + " es menor a 0 o mayor a 100.");
} else {
    alert("El número " + numero + " está en el rango de 0 a 100.");
}