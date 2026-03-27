
dia = parseInt(prompt("Introduce un número del 1 al 7:"))
if (dia >= 1 && dia <= 7) {

    if (dia === 6 || dia === 7) {
        alert("Es Fin de semana")
    } else {
        alert("Es un día laboral")
    }

} else {
    alert("Número inválido. Por favor, elige del 1 al 7.")
}