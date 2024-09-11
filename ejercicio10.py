from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/traza/<string:izquierda_a_derecha>")
def traza(izquierda_a_derecha):
    matriz = json.loads(request.args.get('matriz'))
    length = len(matriz)
    esCuadrada = True
    suma = 0
    for fila in matriz:
        if len(fila) != length:
            esCuadrada = False
            return jsonify(esCuadrada = esCuadrada)
        
    if(esCuadrada):
        if izquierda_a_derecha == "true": 
            for i in range(length):
                suma += matriz[i][i]
        else:  
            for i in range(length):
                suma += matriz[i][length - 1 - i]
            
    return jsonify(suma = suma)