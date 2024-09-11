from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route("/intercala")
def posearch():
    arreglo1 = json.loads(request.args.get('arreglo1'))
    arreglo2 = json.loads(request.args.get('arreglo2'))
    desordenado = arreglo1 + arreglo2
    resultado = []
    resultado = sorted(desordenado)
    
    return jsonify({"arreglo": resultado})

