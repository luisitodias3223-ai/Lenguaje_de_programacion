usuario= "luis"
contraseña = "12345"

 usuarioIngresado = prompt("Introduce tu nombre de usuario:");
 contraseñaIngresada = prompt("Introduce tu contraseña:");

if (usuarioIngresado === usuario && contraseñaIngresada === contraseña) {
    alert("Login exitoso. ¡Bienvenido!");
} else {
    alert("Error: Usuario o contraseña incorrectos.")
}