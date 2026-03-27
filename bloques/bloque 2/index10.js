nombre = prompt("Introduce tu nombre de usuario:")

if (nombre === "Admin") {
    alert("¡Bienvenido, Administrador! Tienes acceso total.")
} else {
    alert("Hola, " + nombre + ". Tienes acceso de usuario estándar.")
}