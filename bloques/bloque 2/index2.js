
 entrada = prompt("Ingresa la temperatura actual en °C:")


 temperatura = parseFloat(entrada)

if (temperatura > 30) {
    alert("¡Hace calor! La temperatura es de " + temperatura + "°C.")
    alert("Estado: Caluroso");
} else {
    alert("No hace tanto calor. La temperatura es de " + temperatura + "°C.")
    alert("Estado: Normal o Frío")
}