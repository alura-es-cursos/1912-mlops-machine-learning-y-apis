from flask import Flask
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('casas.csv')
df = df[['area','precio']]
X = df[['area']]
y = df.precio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
modelo = LinearRegression()
modelo.fit(X_train, y_train)


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

@app.route('/precio_casas/<int:area>')
def precio_casas(area):
    precio = modelo.predict([[area]])
    return str(precio)

# Debug On para que el archivo reconozca los cambios sin tener que
# interrumpir la ejecución de main.py

app.run(debug=True) 