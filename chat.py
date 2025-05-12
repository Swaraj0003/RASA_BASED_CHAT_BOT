# backend/routes/chat.py
from flask import Blueprint, render_template, request, jsonify
from backend.database.connection import SessionLocal
from backend.models.user import User
from backend.models.conversation import Conversation
import requests

chat_bp = Blueprint('chat', __name__)
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@chat_bp.route('/')
def index():
    return render_template('index.html')

@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    email = request.form['email']

    session = SessionLocal()
    user = session.query(User).filter(User.email == email).first()

    if not user:
        user = User(name='Unknown', email=email)
        session.add(user)
        session.commit()

    response = requests.post(RASA_URL, json={"sender": email, "message": message})
    bot_response = response.json()[0]['text']

    # Save message and response
    chat = Conversation(user_id=user.id, message=message, response=bot_response)
    session.add(chat)
    session.commit()
    session.close()

    return jsonify({'response': bot_response})
