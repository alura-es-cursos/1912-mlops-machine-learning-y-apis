from flask import Flask
from textblob import TextBlob

app = Flask(__name__) # Forma correcta de colocar el nombre

@app.route('/')
def home():
    return "Mi primera API."

# Crearemos una ruta de acceso, endpoint o la url de nuestra API
# Para habilitar el análisis de sentimiento en la aplicacion .py

@app.route('/sentimiento/<frase>')
def sentimiento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang='es', to='en')
    polaridad = tb_en.sentiment.polarity
    return f'La Polaridad de la frase es: {polaridad}'

# Debug On para que el archivo reconozca los cambios sin tener que
# interrumpir la ejecución de main.py

app.run(debug=True) 