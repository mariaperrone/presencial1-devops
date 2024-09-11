from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/histograma")
def histograma():
    lista = json.loads(request.args.get('arreglo'))

    resultado = []

    for i in range(len(lista)):
        valor = int(lista[i])
        linea = f"{valor}{'*' * valor}"
        resultado.append(linea)

    return jsonify({"histograma": resultado})