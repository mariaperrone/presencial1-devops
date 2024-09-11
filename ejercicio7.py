from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/intercala")
def posearch():
    arreglo1 = json.loads(request.args.get('arreglo1'))
    arreglo2 = json.loads(request.args.get('arreglo2'))
    desordenado = arreglo1 + arreglo2
    resultado = desordenado[:]
    n = len(resultado)
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultado[j] > resultado[j + 1]:
                # Intercambia los elementos
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    
    return jsonify({"arreglo": resultado})

