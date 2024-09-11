#3. Coincidencia de palabra: Escribe una función llamada `coincidencia` que, dada una palabra y una frase,
#cuente cuántas veces aparece esa palabra en la frase. Por ejemplo, si la palabra es 'sol' y la frase es 'el sol
#brilla más que el sol', debe devolver 2.


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





      
