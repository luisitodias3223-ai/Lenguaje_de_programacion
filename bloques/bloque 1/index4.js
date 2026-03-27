// 1. Pedimos los dos números
let n1 = parseFloat(prompt("Ingresa el primer número:"));
let n2 = parseFloat(prompt("Ingresa el segundo número:"));

if (n1 > n2) {
    alert("El primer número (" + n1 + ") es mayor que el segundo (" + n2 + ").");
} else if (n2 > n1) {
    alert("El segundo número (" + n2 + ") es mayor que el primero (" + n1 + ").");
} else if (n1 === n2) {
    alert("Ambos números son iguales.");
} else {
    alert("Por favor, ingresa números válidos.");
}