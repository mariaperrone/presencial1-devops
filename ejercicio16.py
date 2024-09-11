# 16. Contar subcadena: Escribe una función llamada `contarSubcadena` que, dada una cadena y una
# subcadena, cuente cuántas veces aparece la subcadena en la cadena principal. Por ejemplo, en la cadena
# 'banana' y la subcadena 'ana', el resultado sería 1.

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/contar_subcadena/', methods=['GET'])
def contar_subcadena():
    # Obtengo la cadena y la subcadena desde los parámetros de la URL
    # Ejemplo URL: http://127.0.0.1:5000/contar_subcadena/?cadena=caballo&subcadena=ca
    cadena = request.args.get('cadena', '')
    subcadena = request.args.get('subcadena', '')

    # Cuento cuántas veces aparece la subcadena en cadena 
    resultado = cadena.count(subcadena)

    return jsonify({"cadena":cadena,"subcadena": subcadena, "cantidad de veces que aparece": resultado})

if __name__ == '__main__':
    app.run(debug=True)

