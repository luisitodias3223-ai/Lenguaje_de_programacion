
 tempEntrada = prompt("¿Cuál es la temperatura actual en °C?")

temperatura = parseFloat(tempEntrada)


if (temperatura < 15) {
    alert("Hace frío. La temperatura es de " + temperatura + "°C.")
    alert("Estado: Frío")
} else {
    alert("No hace frío. La temperatura es de " + temperatura + "°C.")
    alert("Estado: Templado o Calor")
}