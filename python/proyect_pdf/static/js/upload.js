const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileNameDiv = document.getElementById('file-name');

// Eventos cuando el archivo se arrastra sobre la zona
['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.add('drag-over'); // Añade el estilo visual turquesa
    }, false);
});

// Eventos cuando el archivo sale de la zona o se suelta
['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.remove('drag-over'); // Quita el estilo turquesa
    }, false);
});

// Detectar cuando el archivo ya ha sido seleccionado o soltado
fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        // Escribe el nombre del archivo en la interfaz
        fileNameDiv.textContent = `📄 Archivo listo: ${fileInput.files[0].name}`;
    }
});
