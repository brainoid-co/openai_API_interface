# O1 Browser Interface

This project is a Flask-based web application that provides a chat interface similar to ChatGPT. It uses OpenAI's API to interact with the "o1" model, stores chat history in a SQLite database, and allows setting a custom prompt.

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate


### File Structure
o1_browser_interface/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── database.py
│   ├── models.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── index.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │       └── app.js
├── config.py
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
