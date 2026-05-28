const searchInput = document.getElementById('search-input');
const cards = document.querySelectorAll('.text-card');

searchInput.addEventListener('input', (e) => {
    const valorBusqueda = e.target.value.toLowerCase().trim();

    cards.forEach(card => {
        const textoTarjeta = card.querySelector('.editable-content').textContent.toLowerCase();

        if (textoTarjeta.includes(valorBusqueda)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
});


function procesarYContinuar() {
    const listaModificada = [];

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
            window.location.href = "/preview";
        } else {
            alert("Hubo un problema al procesar el ordenamiento en el servidor.");
        }
    })
    .catch(error => {
        console.error("Error en la petición Fetch:", error);
    });
}
