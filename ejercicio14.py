#14. Traspuesta de una matriz: Escribe una función llamada `traspuesta` que reciba una matriz y devuelva
#su traspuesta, intercambiando filas por columnas. Por ejemplo, la traspuesta de una matriz 2x3 sería una
#matriz 3x2.
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/traspuesta/', methods=['GET'])

def traspuesta():
    
    # Obtengo los valores de la matriz desde los parámetros de la URL
    # Ejemplo URL: http://127.0.0.1:5000/traspuesta/?valores=1&valores=2&valores=3&valores=4&valores=5&valores=6&filas=2&columnas=3
    valores = request.args.getlist('valores', type=int)
    cant_filas = int(request.args.get('filas', 0))
    cant_columnas = int(request.args.get('columnas', 0))
    
    matriz = []

    # 1. Construyo la matriz
    # Recorro la cantidad de filas
    for i in range(cant_filas):
        # Calcular los índices que definen qué elementos de la lista valores pertenecen a cada fila de la matriz.
        inicio = i * cant_columnas
        fin = (i + 1) * cant_columnas

        # Obtener los valores de la fila
        fila = valores[inicio:fin]

        # Agreggo la fila a la matriz
        matriz.append(fila)

    matriz_traspuesta = []

    # Recorro las columnas de matriz y voy a ir agregando filas a matriz_traspuesta
    for j in range(cant_columnas):
        
        fila_matriz_traspuesta = []
        
        # Recorremos las filas de matriz 
        for i in range(cant_filas):
            # Agrego el valor de la fila i, columna j a la fila de la matriz traspuesta
            fila_matriz_traspuesta.append(matriz[i][j])
        
        # Añadir la fila a la matriz traspuesta
        matriz_traspuesta.append(fila_matriz_traspuesta)

    return jsonify({"matriz_traspuesta": matriz_traspuesta})

if __name__ == '__main__':
    app.run(debug=True)
