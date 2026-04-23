from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        try:
            # Entrada de datos
            a = float(request.form.get('num1'))
            b = float(request.form.get('num2'))
            operacion = request.form.get('operacion')
            nombre = ""
            c = 0

            # Lógica de transformación
            if operacion == "**":
                c = a ** b
                nombre = "Potencia"
            elif operacion == "*":
                c = a * b
                nombre = "Multiplicación"
            elif operacion == "+":
                c = a + b
                nombre = "Suma"
            elif operacion == "-":
                c = a - b
                nombre = "Resta"
            elif operacion == "%":
                c = a % b
                nombre = "Resto"
            elif operacion == "//":
                c = a // b
                nombre = "División entera"
            elif operacion == "/":
                nombre = "División"
                if b != 0:
                    c = a / b
                else:
                    c = "No se puede dividir por 0"
            else:
                c = "Operación no reconocida"

            resultado = {"res": c, "op": nombre}

        except (ValueError, TypeError):
            resultado = {"res": "Error: Ingresa solo números", "op": "Error"}

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
