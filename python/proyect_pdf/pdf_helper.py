import pdfplumber
from fpdf import FPDF
import re

def extraer_texto(ruta_pdf):
    """Abre el PDF."""
    lineas_extraidas = []
    with pdfplumber.open(ruta_pdf) as pdf:
        for pagina in pdf.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                for linea in texto_pagina.split("\n"):
                    if linea.strip():
                        lineas_extraidas.append(linea.strip())
    return lineas_extraidas


def ordenar_asistencia(lineas):
    """
    Algoritmo:
    """
    datos_parseados = []
    
    for linea in lineas:
        numeros = re.findall(r'\d+', linea)
        cedula_str = "".join(numeros)
        
        texto_limpio = re.sub(r'[\d\.\-]', '', linea).strip()
        texto_limpio = re.sub(r'^(V|E)\b', '', texto_limpio, flags=re.IGNORECASE).strip()
        
        palabras = texto_limpio.split()
        
        if len(palabras) >= 2:
            apellido = palabras[0]
            nombre = " ".join(palabras[1:])
        elif len(palabras) == 1:
            apellido = palabras[0]
            nombre = "N/A"
        else:
            apellido = "SIN APELLIDO"
            nombre = "SIN NOMBRE"
            
        datos_parseados.append({
            'apellido': apellido.upper(),
            'nombre': nombre.upper(),
            'cedula': int(cedula_str) if cedula_str.isdigit() else 0
        })
    
    datos_ordenados = sorted(datos_parseados, key=lambda x: (x['apellido'], x['nombre'], x['cedula']))
    
    lineas_procesadas = []
    for d in datos_ordenados:
        cedula_formateada = f"{d['cedula']:,}".replace(",", ".") if d['cedula'] > 0 else "S/C"
        lineas_procesadas.append(f"{d['nombre']}, {d['apellido']} - C.I: {cedula_formateada}")
        
    return lineas_procesadas


def generar_pdf_final(lineas_ordenadas, ruta_salida):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=11) 
    pdf.image("static/logo_unefa.png", x=10, y=10, w=40)
    
    # Encabezado
    pdf.cell(0, 6, "REPÚBLICA BOLIVARIANA DE VENEZUELA", ln=True, align="C")
    pdf.cell(0, 6, "UNIVERSIDAD NACIONAL EXPERIMENTAL POLITÉCNICA", ln=True, align="C")
    pdf.cell(0, 6, "DE LA FUERZA ARMADA NACIONAL BOLIVARIANA (UNEFA)", ln=True, align="C")
    pdf.cell(0, 6, "CARACAS, 15/05/26 ", ln=True, align="C")
    
    pdf.ln(12)
    pdf.set_font("Helvetica", 'B', size=13)
    pdf.cell(0, 10, "REPORTE DE ASISTENCIA TÉCNICA ORDENADA", ln=True, align="C")
    pdf.ln(6)
    
    pdf.set_font("Helvetica", size=11)
    for i, linea in enumerate(lineas_ordenadas, 1):
        pdf.cell(0, 8, f"{i}. {linea}", ln=True)
        
    pdf.output(ruta_salida)