from flask import Flask, request, jsonify, render_template_string, make_response
import re
import os
import json

app = Flask(__name__)
latest_tokens = []  # Últimos tokens procesados

@app.route("/tokenize", methods=["POST"])
def tokenize():
    global latest_tokens
    data = request.get_json()
    text = data.get("text", "")
    latest_tokens = simple_tokenize(text)
    return jsonify({"tokens": latest_tokens})

@app.route("/log", methods=["GET"])
def show_tokens_html():
    html = """
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>Últimos Tokens</title></head>
    <body>
        <h2>Últimos tokens procesados:</h2>
        <ul>
            {% for token in tokens %}
            <li>{{ token }}</li>
            {% endfor %}
        </ul>
        <a href="/download">Descargar JSON</a>
    </body>
    </html>
    """
    return render_template_string(html, tokens=latest_tokens)

@app.route("/download", methods=["GET"])
def download_json():
    response = make_response(json.dumps({"tokens": latest_tokens}, indent=2))
    response.headers.set("Content-Type", "application/json")
    response.headers.set("Content-Disposition", "attachment", filename="tokens.json")
    return response

def simple_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
