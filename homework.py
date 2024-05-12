#In this file, I have developed flask application.
import json
from flask import Flask, jsonify, request
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


@app.route('/api/v2/get/data', methods=['GET'])
def get_data():
    with open('sample.json', 'r') as file:
        json_data = json.load(file)
    return jsonify(json_data)
    #     json_object = jsonify(file)
    # return json_object


# @app.route('/api/v2/add/data', methods=['POST'])
# def post_data():
#     data = request.json
#     if data is None:
#         return jsonify({'error': 'No JSON data received'}), 400
#     else:
#         with open("sample.json", "w") as outfile:
#             outfile.write(data)
#         return jsonify({'message': 'Message received'}), 200
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
# @app.route('/api/v2/get/data', methods=['GET'])
# def get_data():
#     with open('sample.json', 'r') as file:
#         json_object = json.load(file)
#     return jsonify(json_object)

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