from flask import Flask, jsonify

app = Flask(__name__)

# Simulated parking data
parking_slots = {
    "Location A": {"available": 5, "total": 10},
    "Location B": {"available": 2, "total": 8},
    "Location C": {"available": 0, "total": 12}
}

@app.route('/')
def home():
    return "Welcome to ParkSmart - AI-powered Parking Optimization"

@app.route('/api/availability')
def availability():
    return jsonify(parking_slots)

if __name__ == '__main__':
    app.run(debug=True)
