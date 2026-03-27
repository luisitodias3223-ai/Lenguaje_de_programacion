
let num1 = parseFloat(prompt("Ingresa el primer número:"));
let num2 = parseFloat(prompt("Ingresa el segundo número:"));
if (num1 === num2) {
    alert("¡Los números son iguales!");
    alert(num1 + " es igual a " + num2);
} else {
    alert("Los números son diferentes.");
    alert(num1 + " no es igual a " + num2);
}