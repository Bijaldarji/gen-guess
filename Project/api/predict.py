# api/predict.py

from flask import Flask, request, jsonify
from app import app, predict  # Import the Flask app and the predict function

@app.route('/api/predict', methods=['POST'])
def handler():
    data = request.get_json()
    text = data['text']
    return jsonify(predict(text))  # Call the predict function from your Flask app

