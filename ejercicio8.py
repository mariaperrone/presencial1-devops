from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/fibo/<int:n>")
def fibo(n):
    secuencia = []
    
    if n <= 0:
        return secuencia
    elif n == 1:
        return [0]
    
    secuencia = [0, 1]
    
    for i in range(2, n+1):
        num = secuencia[i - 1] + secuencia[i - 2]
        secuencia.append(num)
    
    return jsonify(fibonacci = secuencia)
