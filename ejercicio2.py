from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/invertir/<palabra>")
def invertir(palabra):
    lista = list(palabra)
    length = len(lista)
    for i in range(length // 2):
        lista[i], lista[length - i - 1] = lista[length - i - 1], lista[i]
    return jsonify(resultado = ''.join(lista))