// 1. Pedimos el número
let numero = parseInt(prompt("Ingresa un número para saber si es par:"));

if (numero % 2 === 0) {
    alert("El número " + numero + " es par.");
    alert("Resultado: Par");
} else {
    alert("El número " + numero + " es impar.");
    alert("Resultado: Impar");
}