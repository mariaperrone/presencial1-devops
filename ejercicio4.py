from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/maximin")
def maximin():
    lista = json.loads(request.args.get('lista'))
    mayor_numero = 0
    posicion = []
    for indice, valor in enumerate(lista):
        if valor > mayor_numero:
            mayor_numero = valor
            posicion = [indice]
        elif valor == mayor_numero:
            posicion.append(indice)
    return jsonify(mayor_numero = mayor_numero, posicion = posicion)