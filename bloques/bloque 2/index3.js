hora = parseInt(prompt("Introduce una hora (0-23):"))

if (hora >= 0 && hora <= 23) {
    
    if (hora < 12) {
        alert("Es AM")
    } else {
        alert("Es PM")
    }

} else {
    alert("Esa hora no es válida. Debe estar entre 0 y 23.")
}