#13. Punto de silla: Escribe una función llamada `silla` que encuentre los puntos de silla en una matriz.
#Un punto de silla es un elemento que es el mínimo de su fila y el máximo de su columna
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/punto_de_silla/', methods=['GET'])
def punto_de_silla():
    
    # Obtengo los valores de la matriz desde los parámetros de la URL
    # Ejemlo de la URL: http://127.0.0.1:5000/punto_de_silla/?valores=1&valores=2&valores=3&valores=4&valores=5&valores=6&valores=7&valores=8&valores=9&filas=3&columnas=3
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

    # 2. Calculo los puntos de silla
    puntos_silla = []

    # Recorro cada fila de la matriz
    for i in range(len(matriz)):
        # Calculo el mínimo valor de la fila
        valor_min_fila = min(matriz[i])
        # Guardo el índice de la columna donde se encuentra el mínimo valor
        col_idx_valor_min_fila = matriz[i].index(valor_min_fila)

        # Variable para guardar si el valor es el máximo en su columna
        es_maximo_columna = True

        # Recorro cada fila de la matriz para verificar si es el máximo en su columna
        for j in range(len(matriz)):
            if valor_min_fila < matriz[j][col_idx_valor_min_fila]:
                es_maximo_columna = False
                break  # Si encuentro un valor mayor corto
        
        # Si es el máximo de su columna, lo agrego como un punto de silla
        if es_maximo_columna:
            puntos_silla.append((i, col_idx_valor_min_fila, valor_min_fila))

    return jsonify({"puntos_silla": puntos_silla})

if __name__ == '__main__':
    app.run(debug=True)
