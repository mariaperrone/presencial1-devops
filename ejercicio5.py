from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/posearch")
def posearch():
    lista = json.loads(request.args.get('arreglo'))
    numero = int(request.args.get('buscar'))
    cercano = lista[0]
    posicion = 0
    for i in range(len(lista)):
        if abs(int(lista[i]) - numero) < abs(cercano - numero):
            cercano = lista[i]
            posicion = i
    return jsonify({"posicion": posicion, "numero": cercano})