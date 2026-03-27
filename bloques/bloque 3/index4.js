nota = parseInt(prompt("Introduce tu nota (0-100):"))

if (nota >= 90 && nota <= 100) {
    alert("¡Resultado Excelente! Has alcanzado el nivel más alto.")
} else if (nota >= 0 && nota < 90) {
    alert("Tu nota es buena, pero no llega a Excelente.")
} else {
    alert("Error: La nota debe estar entre 0 y 100.")
}