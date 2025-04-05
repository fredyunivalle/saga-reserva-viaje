from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

FLIGHT_URL = "http://flight_service:5001"
HOTEL_URL = "http://hotel_service:5002"
CAR_URL = "http://car_service:5003"

@app.route('/book-trip', methods=['POST'])
def book_trip():
    user = request.json.get('user')
    successful_steps = []

    try:
        # Reservar vuelo
        res = requests.post(f"{FLIGHT_URL}/reserve", json={"user": user})
        if res.status_code != 200:
            raise Exception("Error en vuelo")
        successful_steps.append("flight")

        # Reservar hotel
        res = requests.post(f"{HOTEL_URL}/reserve", json={"user": user})
        if res.status_code != 200:
            raise Exception("Error en hotel")
        successful_steps.append("hotel")

        # Reservar carro
        res = requests.post(f"{CAR_URL}/reserve", json={"user": user})
        if res.status_code != 200:
            raise Exception("Error en carro")
        successful_steps.append("car")

        return jsonify({"message": f"Reserva completada para {user}"}), 200

    except Exception as e:
        print(f"❌ Error: {e}")
        # Compensar pasos exitosos
        if "car" in successful_steps:
            requests.post(f"{CAR_URL}/cancel", json={"user": user})
        if "hotel" in successful_steps:
            requests.post(f"{HOTEL_URL}/cancel", json={"user": user})
        if "flight" in successful_steps:
            requests.post(f"{FLIGHT_URL}/cancel", json={"user": user})
        return jsonify({"message": f"Error en la reserva para {user}. Se ejecutaron compensaciones."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
