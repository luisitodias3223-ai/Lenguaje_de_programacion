 nota1 = parseFloat(prompt("Introduce la primera nota:"))
 nota2 = parseFloat(prompt("Introduce la segunda nota:"))

if (nota1 > 90 || nota2 > 90) {
    alert("¡Felicidades! Estás Becado.")
} else {
    alert("No cumples con el requisito de excelencia para la beca.");
}