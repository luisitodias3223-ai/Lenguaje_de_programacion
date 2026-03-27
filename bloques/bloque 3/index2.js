// 1. Pedimos los datos
edad = parseInt(prompt("¿Cuántos años tienes?"))
tieneLicencia = prompt("¿Tienes licencia de conducir? (si/no)")

if (edad >= 18 && tieneLicencia === "si") {
    alert("Puedes conducir. ¡Buen viaje!")
} else {
    alert("No puedes conducir.")
}