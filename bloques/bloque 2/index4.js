
calificacion = parseInt(prompt("Introduce tu calificación (0-100):"))

if (calificacion >= 0 && calificacion <= 100) {

    if (calificacion >= 70) {
        alert("¡Felicidades! Has aprobado.")
    } else {
        alert("Lo siento, no has aprobado.")
    }

} else {
    alert("Por favor, introduce una calificación válida entre 0 y 100.")
}