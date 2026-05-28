from flask import Flask, render_template, request, redirect, url_for, session, send_file
import os
from werkzeug.utils import secure_filename
from pdf_helper import extraer_texto, ordenar_asistencia, generar_pdf_final

app = Flask(__name__)
app.secret_key = "unefa_sistemas_key_secreta"

UPLOAD_FOLDER = 'temp_uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 1. Interfaz 1: Vista de subida
@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'asistencia_pdf' not in request.files:
        return "Error: No se envió ningún archivo.", 400
    archivo = request.files['asistencia_pdf']
    if archivo.filename == '':
        return "Error: No has seleccionado ningún archivo.", 400
        
    if archivo and archivo.filename.lower().endswith('.pdf'):
        nombre_seguro = secure_filename(archivo.filename)
        ruta_completa = os.path.join(app.config['UPLOAD_FOLDER'], nombre_seguro)
        archivo.save(ruta_completa)
        
        session['lineas_asistencia'] = extraer_texto(ruta_completa)
        
        return redirect(url_for('manage'))
    return "Error: Formato no permitido.", 400

@app.route('/manage')
def manage():
    datos = session.get('lineas_asistencia', [])
    return render_template('manage.html', lista_lineas=datos)

@app.route('/save_edited', methods=['POST'])
def save_edited():
    datos_recibidos = request.get_json()
    lineas_raw = datos_recibidos.get('lineas', [])
    session['lineas_ordenadas'] = ordenar_asistencia(lineas_raw)
    return {"status": "success"}

@app.route('/preview')
def preview():
    datos_finales = session.get('lineas_ordenadas', [])
    return render_template('preview.html', lista_final=datos_finales)

@app.route('/download_pdf')
def download_pdf():
    datos_finales = session.get('lineas_ordenadas', [])
    if not datos_finales:
        return "No hay datos listos", 400
    ruta_salida = os.path.join(app.config['UPLOAD_FOLDER'], "reporte_asistencia_unefa.pdf")
    generar_pdf_final(datos_finales, ruta_salida)
    return send_file(ruta_salida, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
