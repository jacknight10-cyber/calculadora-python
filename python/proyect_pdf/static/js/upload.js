const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileNameDiv = document.getElementById('file-name');

['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.add('drag-over'); 
    }, false);
});

['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropZone.classList.remove('drag-over'); 
    }, false);
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        fileNameDiv.textContent = `📄 Archivo listo: ${fileInput.files[0].name}`;
    }
});
