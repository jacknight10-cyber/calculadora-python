const searchInput = document.getElementById('search-input');
const cards = document.querySelectorAll('.text-card');

// 🔍 FILTRO EN TIEMPO REAL
searchInput.addEventListener('input', (e) => {
    const valorBusqueda = e.target.value.toLowerCase().trim();

    cards.forEach(card => {
        // Obtenemos el texto dentro del área editable de la tarjeta
        const textoTarjeta = card.querySelector('.editable-content').textContent.toLowerCase();

        // Si el texto incluye lo que busca el usuario, la muestra; si no, la oculta
        if (textoTarjeta.includes(valorBusqueda)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
});

// 🚀 FUNCIÓN PREPARATORIA PARA EL SIGUIENTE PASO
// ... (El código del buscador que hiciste en el paso anterior se queda igual arriba)

function procesarYContinuar() {
    const listaModificada = [];

    // Recorremos las tarjetas editables en pantalla
    cards.forEach(card => {
        const contenido = card.querySelector('.editable-content').innerText.trim();
        if (contenido) {
            listaModificada.push(contenido);
        }
    });

    if (listaModificada.length === 0) {
        alert("El documento no contiene líneas de texto válidas.");
        return;
    }

    // 🔌 CONEXIÓN: Enviamos el JSON al backend de Flask
    fetch('/save_edited', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ lineas: listaModificada })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            // Si el servidor procesó y ordenó todo bien, saltamos a la Interfaz 3
            window.location.href = "/preview";
        } else {
            alert("Hubo un problema al procesar el ordenamiento en el servidor.");
        }
    })
    .catch(error => {
        console.error("Error en la petición Fetch:", error);
    });
}
