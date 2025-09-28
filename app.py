from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

feedback_list = []

@app.route('/feedback', methods=['POST'])
def receive_feedback():
    data = request.json
    feedback_list.append(data)
    return jsonify({"message": "Feedback received!", "data": data}), 200

@app.route('/feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback_list), 200

@app.route('/')
def serve_form():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

