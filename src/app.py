from flask import Flask, request, jsonify
import json
import jsonschema
from jsonschema import validate
from utils import openai, firebase

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json

        with open('schemas/chat_request_schema.json') as f:
            validate(data, json.load(f))

    except jsonschema.exceptions.ValidationError as err:
        return jsonify({"error": err.message}), 400

    completion, nearest_neighbor = openai.get_completion(messages=[data])

    firebase.set_input(
        user_input=data['question'],
        nearest_neighbor=nearest_neighbor,
        completion=completion)

    return jsonify({
        "question": data['question'],
        "answer": completion,
        "recommendations": openai.get_article_recommendations(' Pregunta: ' + data['question'] + '\n\n###\n\n Respuesta: ' + completion),
        "contact": "Contáctanos por:\n\nWhatsApp: +34 667 662 551. L-J de 9:00h a 18:00h. V de 9:00h a 15:00h.\nTelegram: +34 667 662 551. L-J 9:00h a 18:00 h. V de 9:00h a 15:00h.\nFacebook: contacta con nosotros por mensaje privado, recibirás respuesta en menos de 48 horas.\nSkype: para personas de fuera de Barcelona. Videoconferencia o llamada de voz. Búscanos en nuestra cuenta en Skype (gttvih). Tiempo máximo de consulta: 45 minutos. Requiere cita previa solicitándola por teléfono (+34 934 582 641), email (consultas@gtt-vih.org) o cuenta Skype.\nHangouts: aplicación de mensajería instantánea de Google+, y destaca su sistema de llamadas telefónicas y de videoconferencia. Es gratis y se necesita un teléfono u ordenador.\n\nTiempo máximo de consulta: 45 minutos Requiere cita previa solicitándola por teléfono (+34 934 582 641), email (consultas@gtt-vih.org) o cuenta HangOut."
    }), 200

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True)