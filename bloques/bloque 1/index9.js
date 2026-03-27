// 1. Pedimos el número al usuario
let numero = parseInt(prompt("Ingresa un número para saber si es múltiplo de 5:"));

if (numero % 5 === 0) {
    alert("Sí, el número " + numero + " es múltiplo de 5.");
    alert(numero + " es múltiplo de 5.");
} else {
    alert("No, el número " + numero + " no es múltiplo de 5.");
    alert(numero + " no es múltiplo de 5.");
}