from flask import Flask, request, jsonify
from pymongo import MongoClient
import uuid
import available_vehicles

app = Flask(__name__)

# Set up mongo connection
client = MongoClient("mongodb://localhost:27017/")
db = client["G_wheels"]
Vehicle_booking = db["Bookings"]

# Route to add a new booking
@app.route('/bookings', methods=['POST'])
def add_booking():
    data = request.get_json()
    booking = {
        'id': str(uuid.uuid4()),
        'customer_name': data['customer_name'],
        'pick_up': data['pick_up'],
        'drop': data['drop']
    }
    booking.insert_one(booking)
    return jsonify({'message': 'available vehicles'}),
# for vehicle list
    


# Run the application
if __name__ == '__main__':
    app.run(debug=True)