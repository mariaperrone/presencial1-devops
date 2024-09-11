from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/esCuadrada")
def esCuadrada():
    matriz = json.loads(request.args.get('matriz'))
    length = len(matriz)
    esCuadrada = True
    for fila in matriz:
        if len(fila) != length:
            esCuadrada = False
    return jsonify(esCuadrada = esCuadrada)