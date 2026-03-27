// 1. Solicitamos la edad al usuario
let edadInput = prompt("¿Cuántos años tienes?");

let edad = parseInt(edadInput);

if (edad > 18) {
    alert("Eres mayor de 18 años.");
    alert("Acceso concedido: Mayor de 18.");
} else if (edad === 18) {
    alert("Tienes exactamente 18 años.");
} else {
    alert("Eres menor de 18 años.");
    alert("Acceso denegado: Menor de edad.");
}