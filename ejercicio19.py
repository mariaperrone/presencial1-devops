from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/ordenarPorLongitud")
def ordenarPorLongitud():
    lista = json.loads(request.args.get('lista'))
    return sorted(lista, key=len)