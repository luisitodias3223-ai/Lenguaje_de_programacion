color = prompt("Introduce un color:").toLowerCase()

if (color === "rojo" || color === "amarillo" || color === "azul") {
    alert("¡Correcto! El " + color + " es un color primario.")
} else {
    alert("El " + color + " no es un color primario (o al menos no de los tradicionales).")
}