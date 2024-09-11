from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/primo/<int:n>")
def es_primo(n):
    if n <= 1:
        return jsonify(primo = False)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return jsonify(primo = False)
    return jsonify(primo = True)