from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

modelo = pickle.load(open('modelo.pkl','rb'))

columnas = ['area','modelo','estacionamiento']

app = Flask(__name__) 

from flask_basicauth import BasicAuth
app.config['BASIC_AUTH_USERNAME'] = 'alvaro'
app.config['BASIC_AUTH_PASSWORD'] = 'alura'
basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Mi primera API."

@app.route('/sentimiento/<frase>')
@basic_auth.required

def sentimiento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang='es', to='en')
    polaridad = tb_en.sentiment.polarity
    return f'La Polaridad de la frase es: {polaridad}'

@app.route('/precio_casas/',methods=['POST'])
def precio_casas():
    datos = request.get_json()
    datos_input = [datos[col] for col in columnas]
    precio = modelo.predict([datos_input])
    return jsonify(precio= precio[0])

app.run(debug=True) 
