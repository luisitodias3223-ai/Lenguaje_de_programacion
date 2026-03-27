// 1. Pedimos los dos números al usuario
let dividendo = parseFloat(prompt("Ingresa el primer número (dividendo):"));
let divisor = parseFloat(prompt("Ingresa el segundo número (divisor):"));

if (divisor === 0) {
    alert("Error: No se puede dividir por cero.");
} else if (dividendo % divisor === 0) {
    alert(dividendo + " es divisible por " + divisor + ".");
    alert("Resultado: División exacta.");
} else {
    alert(dividendo + " NO es divisible por " + divisor + ".");
    alert("Resultado: División con residuo.");
}