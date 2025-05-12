from flask import Flask, render_template, request, jsonify
from backend.database.connection import init_db, SessionLocal
from backend.models.user import User
import requests

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Send to Rasa bot
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",
        json={"sender": "user", "message": user_message}
    )
    bot_reply = response.json()[0]['text'] if response.json() else "I didn't understand that."

    return jsonify({"reply": bot_reply})

@app.route('/save-user', methods=['POST'])
def save_user():
    data = request.json
    session = SessionLocal()
    new_user = User(name=data['name'], email=data['email'], enquiry=data['enquiry'])
    session.add(new_user)
    session.commit()
    session.close()
    return jsonify({"message": "Enquiry submitted!"})

if __name__ == '__main__':
    app.run(debug=True)

