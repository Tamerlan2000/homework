from flask import Flask, jsonify, request
from parser import JSONParser

app = Flask(__name__)

@app.route('/api/v2/get/data', methods=['GET'])
def get_data():
    message = "Hello, World!"  # Define a message to include in the response
    return jsonify({'response': 'Received message: ' + message})

@app.route('/api/v2/add/data', methods=['POST'])
def post_data():
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400
    message = data.get('message', 'no message')
    return jsonify({'response': 'Message received: ' + message})

if __name__ == '__main__':
    app.run(debug=True)
