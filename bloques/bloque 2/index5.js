
precio = parseFloat(prompt("Introduce el precio del artículo:"))

if (precio > 0) {
    
    if (precio > 100) {
        alert("Es caro")
    } else {
        alert("Es económico")
    }

} else {
    alert("Por favor, introduce un precio válido.")
}