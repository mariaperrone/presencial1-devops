from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/sumarBorde")
def sumarBorde():
    matriz = json.loads(request.args.get('matriz'))
    n = len(matriz)
    if n == 0: 
        return 0
    if n == 1: 
        return matriz[0][0]

    suma = 0

    suma += sum(matriz[0])
    suma += sum(matriz[-1])

    for i in range(1, n - 1):
        suma += matriz[i][0]
        suma += matriz[i][-1]

    return jsonify(suma = suma)