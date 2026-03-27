// 1. Pedimos el dato al usuario
let entrada = prompt("Ingresa un número para verificar si es cero:");

let numero = parseFloat(entrada);

if (numero === 0) {
    alert("El número ingresado es exactamente cero.");
    alert("Estado: Neutro / Cero");
} else {
    alert("El número " + numero + " no es igual a cero.");
    alert("Estado: Diferente de cero");
}