from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/palindromo/cadena', methods=['GET'])
def palindromo():

    cadena = request.args.get('cadena', '')

    longitud_cadena = len(cadena)
    resultado = True  

    # Recorro hasta la mitad de la longitud de la cadena
    for i in range(longitud_cadena // 2):
        if cadena[i] != cadena[longitud_cadena - i - 1]:
            resultado = False
            break #CORTO cuando hay un false

    # Retorno el resultado en formato JSON
    return jsonify({"cadena": cadena, "es_palindromo": resultado})

if __name__ == '__main__':
    app.run(debug=True)
