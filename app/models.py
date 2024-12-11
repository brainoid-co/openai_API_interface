from .database import db
from datetime import datetime

class ChatHistory(db.Model):
    __tablename__ = "chat_history"
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(64), nullable=False, index=True)
    role = db.Column(db.String(16), nullable=False)  # "user" or "assistant"
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class SessionData(db.Model):
    __tablename__ = "session_data"
    session_id = db.Column(db.String(64), primary_key=True)
    custom_prompt = db.Column(db.Text, nullable=True)
