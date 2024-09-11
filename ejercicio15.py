#15. Suma sobre la diagonal principal: Escribe una función llamada `dpSuma` que tome una matriz
# cuadrada y sume los elementos que están por encima de la diagonal principal, excluyendo la diagonal.

# La diagonal principal de una matriz es aquella que va desde la esquina superior izquierda hasta la esquina inferior derecha.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma_diagonal/', methods=['GET'])
def suma_diagonal():
    # Obtengo los valores de la matriz desde los parámetros de la URL
    #Ejemplo URL: http://127.0.0.1:5000/suma_diagonal/?valores=1&valores=3&valores=4&valores=7&valores=2&valores=5&valores=1&valores=20&valores=6&valores=10&valores=3&valores=55&valores=9&valores=7&valores=8&valores=4&filas=4
    valores = request.args.getlist('valores', type=int)
    cant_filas = int(request.args.get('filas', 0))
    cant_columnas = cant_filas

    matriz = []    

    # 1. Construyo la matriz
    # Recorro la cantidad de filas
    for i in range(cant_filas):
        # Calculo los índices que definen qué elementos de la lista valores pertenecen a cada fila de la matriz.
        inicio = i * cant_columnas
        fin = (i + 1) * cant_columnas

        # Obtengo los valores de la fila
        fila = valores[inicio:fin]

        # Agrego la fila a la matriz
        matriz.append(fila)

    # 2. Calculo la suma 
    suma = 0    
    # Recorro la matriz para sumar los elementos por encima de la diagonal principal
    for i in range(cant_filas):
        for j in range(i + 1, cant_filas):
            suma += matriz[i][j]

    return jsonify({"suma_diagonal": suma})

if __name__ == '__main__':
    app.run(debug=True)
