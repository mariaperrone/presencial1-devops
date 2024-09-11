from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/factorial/<int:n>")
def factorial(n):
    resultado = n
    for x in range(1, n):
        resultado *= x
        
    return jsonify(resultado = resultado)