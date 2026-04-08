from flask import Flask, render_template_string
from threading import Thread
import os
import random

app = Flask(__name__)

# Фейковая страница, маскирующаяся под сайт-визитку или API
FAKE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Data Processing API</title>
    <style>body { font-family: Arial; padding: 50px; }</style>
</head>
<body>
    <h1>Data Processing API Server</h1>
    <p>Status: Online</p>
    <p>Version: 1.4.2</p>
    <p>Endpoints are protected.</p>
</body>
</html>
"""

@app.route('/')
def home():
    # Возвращаем реальный HTML, а не просто текст
    return render_template_string(FAKE_HTML)

@app.route('/health')
def health():
    # Эндпоинт для пинга, который выглядит как системный
    return {"status": "healthy", "uptime": "ok", "latency": random.uniform(0.1, 0.5)}

def run():
    # На Hugging Face порт по умолчанию 7860
    port = int(os.environ.get('PORT', 7860))
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
