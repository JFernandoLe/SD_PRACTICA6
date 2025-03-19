from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados del clima
clima_data = {
    "CDMX": {"temperatura": "25°C", "humedad": "50%"},
    "Guadalajara": {"temperatura": "30°C", "humedad": "40%"},
    "Monterrey": {"temperatura": "28°C", "humedad": "45%"}
}

# Ruta para obtener la temperatura de una ciudad
@app.route('/clima', methods=['GET'])
def obtener_clima():
    ciudad = request.args.get('ciudad')
    if ciudad in clima_data:
        return jsonify({"ciudad": ciudad, "datos": clima_data[ciudad]})
    else:
        return jsonify({"error": "Ciudad no encontrada"}), 404

# Ruta para agregar datos de clima de una nueva ciudad
@app.route('/clima', methods=['POST'])
def agregar_clima():
    data = request.json
    ciudad = data.get('ciudad')
    temperatura = data.get('temperatura')
    humedad = data.get('humedad')

    if not ciudad or not temperatura or not humedad:
        return jsonify({"error": "Faltan datos"}), 400

    clima_data[ciudad] = {"temperatura": temperatura, "humedad": humedad}
    return jsonify({"mensaje": "Ciudad agregada", "datos": clima_data[ciudad]}), 201

# Ruta para eliminar datos de clima de una ciudad
@app.route('/clima', methods=['DELETE'])
def eliminar_clima():
    ciudad = request.args.get('ciudad')
    if ciudad in clima_data:
        del clima_data[ciudad]
        return jsonify({"mensaje": f"Ciudad {ciudad} eliminada"}), 200
    else:
        return jsonify({"error": "Ciudad no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
