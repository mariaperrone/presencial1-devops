from statistics import mean, stdev
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/estadistica")
def estadistica():
    lista = json.loads(request.args.get('lista'))
    return jsonify(media = mean(lista), desviacion = stdev(lista))