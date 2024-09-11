from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/coincidencia/<frase>/<palabra>', methods=['GET'])
def coincidencia(palabra, frase):
    contador = 0

    arrayPalabras = frase.split()

    for palabraComparar in arrayPalabras:
        if palabra == palabraComparar:
            contador += 1

    return jsonify({"coincidencias": contador})





      
