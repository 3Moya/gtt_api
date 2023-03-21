from flask import Flask, request, jsonify
import json
import jsonschema
from jsonschema import validate
from src.utils import openai, firebase

app = Flask(__name__)

@app.route('/chat', methods=['GET'])
def chat():
    try:
        data = request.json

        with open('src/schemas/chat_request_schema.json') as f:
            validate(data, json.load(f))

    except jsonschema.exceptions.ValidationError as err:
        return jsonify({"error": err.message}), 400

    completion = openai.get_completion(messages=data['messages'])

    firebase.set_chat(data=data, completion=completion)

    return jsonify({
        "completion": completion,
        "recommendations": []
    })