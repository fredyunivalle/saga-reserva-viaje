from flask import Flask, request, jsonify

app = Flask(__name__)

reservas = []

@app.route('/reserve', methods=['POST'])
def reservar_carro():
    data = request.json
    user = data.get('user')
    reservas.append(user)
    return jsonify({"message": f"Carro reservado para {user}"}), 200

@app.route('/cancel', methods=['POST'])
def cancelar_carro():
    data = request.json
    user = data.get('user')
    if user in reservas:
        reservas.remove(user)
        return jsonify({"message": f"Reserva de carro cancelada para {user}"}), 200
    else:
        return jsonify({"message": f"No hay reserva de carro para {user}"}), 404

@app.route('/reservas', methods=['GET'])
def ver_reservas():
    return jsonify(reservas), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
