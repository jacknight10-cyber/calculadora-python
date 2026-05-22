from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    
        datos_recibidos = request.form.get('edades')
        
        try:
            edad = [int(x.strip()) for x in datos_recibidos.split(',') if x.strip().isdigit()]
            
            if not edad:
                return render_template('index.html', error="Por favor, ingresa al menos un número válido.")
            

            edad = list(set(edad)) 

            if len(edad) == 1:
                max_val = edad[0]
                min_val = edad[0]
            else:
                if edad[0] >= edad[1]:
                    max_val = edad[0]
                    min_val = edad[1]
                else:
                    max_val = edad[1]
                    min_val = edad[0]

                for i in range(2, len(edad)):
                    if edad[i] > max_val:
                        max_val = edad[i]
                    elif edad[i] < min_val:
                        min_val = edad[i]
            
            return render_template('resultado.html', 
                                   max=max_val, 
                                   min=min_val, 
                                   lista_filtrada=edad)
            
        except Exception as e:
            return render_template('index.html', error="Ocurrió un error al procesar los datos. Verifica el formato.")
            

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
