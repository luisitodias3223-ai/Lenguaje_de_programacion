// 1. Solicitamos el número al usuario
let numero = parseInt(prompt("Ingresa un número para saber si es impar:"));

if (numero % 2 !== 0) {
    alert("El número " + numero + " es impar.");
    alert("Resultado: Impar");
} else {
    alert("El número " + numero + " es par.");
    alert("Resultado: Par");
}