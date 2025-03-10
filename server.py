from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (needed for frontend)

# Sample traffic light states
traffic_lights = {
    "north": "red",
    "south": "red",
    "east": "green",
    "west": "red"
}

@app.route('/update_traffic', methods=['POST'])
def update_traffic():
    data = request.json  # Get data from the frontend (packet information)

    # Simulating packet-based traffic light control
    if data.get("emergency_vehicle") == "true":
        traffic_lights["north"] = "green"
        traffic_lights["south"] = "green"
        traffic_lights["east"] = "red"
        traffic_lights["west"] = "red"
    elif data.get("packet_density") > 50:  # Example threshold
        traffic_lights["east"] = "green"
        traffic_lights["west"] = "red"
    else:
        traffic_lights["east"] = "red"
        traffic_lights["west"] = "green"

    return jsonify(traffic_lights)

@app.route('/get_traffic', methods=['GET'])
def get_traffic():
    return jsonify(traffic_lights)

if __name__ == '__main__':
    app.run(debug=True)