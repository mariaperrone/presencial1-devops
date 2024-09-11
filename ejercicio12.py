from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/sumarEsquinas")
def sumarEsquinas():
    matriz = json.loads(request.args.get('matriz'))
    n = len(matriz)
    if n == 0: 
        return 0
    if n == 1: 
        return matriz[0][0]

    suma = 0

    suma += matriz[0][0]
    suma += matriz[0][-1]
    suma += matriz[-1][0]
    suma += matriz[-1][-1]

    return jsonify(suma = suma)