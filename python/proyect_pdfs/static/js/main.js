function filtrarEstudiantes() {
    // Obtener el texto del buscador y pasarlo a minúsculas
    let input = document.getElementById("txtBuscar");
    let filtro = input.value.toLowerCase();
    
    // Obtener todas las filas de estudiantes de la tabla
    let tabla = document.getElementById("tablaEstudiantes");
    let filas = tabla.getElementsByClassName("fila-estudiante");

    // Recorrer cada fila para verificar si coincide con la búsqueda
    for (let i = 0; i < filas.length; i++) {
        let fila = filas[i];
        // Evaluamos el contenido de texto de toda la fila (Apellido, Nombre, Cédula)
        let textoFila = fila.textContent || fila.innerText;
        
        if (textoFila.toLowerCase().indexOf(filtro) > -1) {
            fila.style.display = ""; // Mostrar fila
        } else {
            fila.style.display = "none"; // Ocultar fila
        }
    }
}
// ... (Aquí se mantiene tu función filtrarEstudiantes anterior)

function agregarFilaEstudiante() {
    // 1. Obtener el cuerpo de la tabla
    let cuerpoTabla = document.getElementById("cuerpoTabla");
    
    // Eliminar el mensaje de "No hay estudiantes" si existe
    let filaVacia = document.getElementById("fila-vacia");
    if (filaVacia) {
        filaVacia.remove();
    }

    // 2. Calcular el número correspondiente al nuevo estudiante
    let totalFilas = cuerpoTabla.getElementsByClassName("fila-estudiante").length;
    let nuevoNumero = totalFilas + 1;

    // 3. Crear el elemento de fila (tr)
    let nuevaFila = document.createElement("tr");
    nuevaFila.className = "fila-estudiante";

    // 4. Inyectar el HTML con los mismos atributos name[] estructurados
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

    // 5. Insertar la nueva fila al final de la tabla
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
