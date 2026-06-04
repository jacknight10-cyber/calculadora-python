function filtrarEstudiantes() {
    let input = document.getElementById("txtBuscar");
    let filtro = input.value.toLowerCase();
    
    let tabla = document.getElementById("tablaEstudiantes");
    let filas = tabla.getElementsByClassName("fila-estudiante");

    for (let i = 0; i < filas.length; i++) {
        let fila = filas[i];
        let textoFila = fila.textContent || fila.innerText;
        
        if (textoFila.toLowerCase().indexOf(filtro) > -1) {
            fila.style.display = ""; // Mostrar fila
        } else {
            fila.style.display = "none"; // Ocultar fila
        }
    }
}

function agregarFilaEstudiante() {
    let cuerpoTabla = document.getElementById("cuerpoTabla");
    
    let filaVacia = document.getElementById("fila-vacia");
    if (filaVacia) {
        filaVacia.remove();
    }

    let totalFilas = cuerpoTabla.getElementsByClassName("fila-estudiante").length;
    let nuevoNumero = totalFilas + 1;

    let nuevaFila = document.createElement("tr");
    nuevaFila.className = "fila-estudiante";

    nuevaFila.innerHTML = `
        <td class="celda-centro número-orden"><strong>${nuevoNumero}</strong></td>
        <td>
            <input type="text" name="apellidos[]" placeholder="EJ. TERAN" required class="input-tabla" style="text-transform: uppercase;">
        </td>
        <td>
            <input type="text" name="nombres[]" placeholder="EJ. JACKSON" required class="input-tabla">
        </td>
        <td>
            <input type="hidden" name="cedulas_originales[]" value="">
            <input type="text" name="cedulas[]" placeholder="EJ. 30693356" required class="input-tabla">
        </td>
    `;

    cuerpoTabla.appendChild(nuevaFila);
}
function actualizarColorRecuadro(selectElement) {
    if (selectElement.value === "P") {
        selectElement.classList.remove("rojo");
        selectElement.classList.add("verde");
    } else {
        selectElement.classList.remove("verde");
        selectElement.classList.add("rojo");
    }
}
