import uuid
import openai
from flask import Blueprint, render_template, request, jsonify, session
from .database import db
from .models import ChatHistory, SessionData
from flask import current_app as app

main = Blueprint('main', __name__)

@main.before_app_request
def ensure_session():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

@main.before_app_first_request
def init_openai_api():
    openai.api_key = app.config["OPENAI_API_KEY"]

@main.route("/", methods=["GET"])
def index():
    session_id = session['session_id']
    # Get chat history
    history = ChatHistory.query.filter_by(session_id=session_id).order_by(ChatHistory.timestamp.asc()).all()

    # Get custom prompt
    session_data = SessionData.query.filter_by(session_id=session_id).first()
    custom_prompt = session_data.custom_prompt if session_data else ""

    return render_template("index.html", history=history, custom_prompt=custom_prompt)

@main.route("/send_message", methods=["POST"])
def send_message():
    user_message = request.form.get("message", "").strip()
    session_id = session['session_id']

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Save user message
    user_chat = ChatHistory(session_id=session_id, role="user", message=user_message)
    db.session.add(user_chat)
    db.session.commit()

    # Retrieve history for model input
    history = ChatHistory.query.filter_by(session_id=session_id).order_by(ChatHistory.timestamp.asc()).all()
    messages = [{"role": h.role, "content": h.message} for h in history]

    # Get custom prompt
    session_data = SessionData.query.filter_by(session_id=session_id).first()
    system_prompt = session_data.custom_prompt if session_data and session_data.custom_prompt else ""
    if system_prompt:
        messages.insert(0, {"role": "system", "content": system_prompt})

    # Call OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        assistant_message = response.choices[0].message.content.strip()
    except Exception as e:
        assistant_message = "Error contacting the model. Please try again."
        print(e)

    # Save assistant response
    assistant_chat = ChatHistory(session_id=session_id, role="assistant", message=assistant_message)
    db.session.add(assistant_chat)
    db.session.commit()

    return jsonify({"message": assistant_message})

@main.route("/save_prompt", methods=["POST"])
def save_prompt():
    custom_prompt = request.form.get("custom_prompt", "").strip()
    session_id = session['session_id']

    session_data = SessionData.query.filter_by(session_id=session_id).first()
    if not session_data:
        session_data = SessionData(session_id=session_id, custom_prompt=custom_prompt)
        db.session.add(session_data)
    else:
        session_data.custom_prompt = custom_prompt

    db.session.commit()
    return jsonify({"status": "success", "prompt": custom_prompt})

