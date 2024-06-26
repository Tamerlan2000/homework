import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v2/get/data', methods=['GET'])
def get_data():
    with open('sample.json', 'r') as file:
        json_data = json.load(file)
    return jsonify(json_data)

@app.route('/api/v2/add/data', methods=['POST'])
def post_data():
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data received'}), 400
    else:
        with open("sample.json", "w") as outfile:
            json.dump(data, outfile)
        return jsonify({'message': 'Message received'}), 200

if __name__ == '__main__':
    app.run(debug=True)