import pdfplumber
from fpdf import FPDF
import re

def extraer_texto(ruta_pdf):
    """Abre el PDF original y extrae sus líneas de texto."""
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
    Algoritmo técnico de ordenamiento:
    Aísla la cédula, separa los apellidos de los nombres,
    y ordena alfabéticamente.
    """
    datos_parseados = []
    
    for linea in lineas:
        # 1. Extraer los números correlativos de la Cédula de Identidad
        numeros = re.findall(r'\d+', linea)
        cedula_str = "".join(numeros)
        
        # 2. Limpiar el texto removiendo números, puntos y guiones
        texto_limpio = re.sub(r'[\d\.\-]', '', linea).strip()
        # Remover letras sueltas 'V' o 'E' indicadoras de nacionalidad al inicio
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
    
    # 3. ORDENAR
    datos_ordenados = sorted(datos_parseados, key=lambda x: (x['apellido'], x['nombre'], x['cedula']))
    
    # 4. Formatear las cadenas de texto limpias
    lineas_procesadas = []
    for d in datos_ordenados:
        cedula_formateada = f"{d['cedula']:,}".replace(",", ".") if d['cedula'] > 0 else "S/C"
        # 🚀 CORRECCIÓN: Cambiado '—' por un guion normal '-' ejecutable por fuentes estándar
        lineas_procesadas.append(f"{d['nombre']}, {d['apellido']} - C.I: {cedula_formateada}")
        
    return lineas_procesadas


def generar_pdf_final(lineas_ordenadas, ruta_salida):
    """Genera el documento PDF final con formato institucional."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=11) 
    pdf.image("static/logo_unefa.png", x=10, y=10, w=40)# Usamos explícitamente Helvetica para evitar mapeos raros
    
    # Encabezado institucional
    pdf.cell(0, 6, "REPÚBLICA BOLIVARIANA DE VENEZUELA", ln=True, align="C")
    pdf.cell(0, 6, "UNIVERSIDAD NACIONAL EXPERIMENTAL POLITÉCNICA", ln=True, align="C")
    pdf.cell(0, 6, "DE LA FUERZA ARMADA NACIONAL BOLIVARIANA (UNEFA)", ln=True, align="C")
    pdf.cell(0, 6, "CARACAS, 15/05/26 ", ln=True, align="C")
    pdf.cell(0, 6, "CATEDRA: LENGUAJE DE PROGRAMACION", ln=True, align="C")
    pdf.cell(0, 6, "PROFESOR: WILLMER CALMAUTA", ln=True, align="C")
    
    pdf.ln(12)
    pdf.set_font("Helvetica", 'B', size=13)
    pdf.cell(0, 10, "REPORTE DE ASISTENCIA TÉCNICA ORDENADA", ln=True, align="C")
    pdf.ln(6)
    
    # Listado numerado
    pdf.set_font("Helvetica", size=11)
    for i, linea in enumerate(lineas_ordenadas, 1):
        pdf.cell(0, 8, f"{i}. {linea}", ln=True)
        
    pdf.output(ruta_salida)