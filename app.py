from flask import Flask, request, jsonify

app = Flask(__name__)
datos = []

@app.route("/")
def home():
    return "<h2>Servidor activo</h2>"

@app.route("/recibir", methods=["POST"])
def recibir():
    data = request.json
    datos.append(data)
    print("📥 Dato recibido:", data)
    return jsonify({"estado": "recibido"}), 200

@app.route("/ver", methods=["GET"])
def ver():
    return jsonify(datos), 200

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

