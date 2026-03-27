estatura = parseInt(prompt("Introduce tu estatura en cm (ejemplo: 175):"))

if (estatura > 0 && estatura < 300) {


    if (estatura > 180) {
        alert("Es una persona alta.")
    } else {
        alert("No es una persona alta.")
    }

} else {
    alert("Por favor, introduce una estatura válida en centímetros.")
}