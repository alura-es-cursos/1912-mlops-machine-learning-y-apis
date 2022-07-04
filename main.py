from flask import Flask

app = Flask('mi_app')

@app.route('/')

def home():
    return "Mi primera API."

app.run()