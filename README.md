# OpenAI API Interface

This project is a Flask-based web application that provides a chat interface similar to ChatGPT. It uses OpenAI's API to interact with the gpt models, stores chat history in a SQLite database, and allows setting a custom prompt.

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
 
2. Create a .env file with the following variables:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

## Run

To run the application, use the following command:
   ```bash
   python run.py
   ```
Then open your browser and go to http://localhost:5000.

### File Structure

```
OpenAI_API_Interface/
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

```

