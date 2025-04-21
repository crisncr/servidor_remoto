from flask import Flask, request, jsonify

app = Flask(__name__)

orden_actual = ""
respuesta = ""

@app.route("/")
def home():
    return "<h2>Servidor activo</h2>"

@app.route("/enviar-orden", methods=["POST"])
def enviar_orden():
    global orden_actual
    orden = request.json.get("orden")
    orden_actual = orden
    return jsonify({"estado": "orden recibida"}), 200

@app.route("/obtener-orden", methods=["GET"])
def obtener_orden():
    return jsonify({"orden": orden_actual}), 200

@app.route("/enviar-respuesta", methods=["POST"])
def recibir_respuesta():
    global respuesta
    respuesta = request.json.get("respuesta")
    return jsonify({"estado": "respuesta recibida"}), 200

@app.route("/ver-respuesta", methods=["GET"])
def ver_respuesta():
    return jsonify({"respuesta": respuesta}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
