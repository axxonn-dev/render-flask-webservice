from flask import Flask, request, jsonify, render_template_string
import re
import os

app = Flask(__name__)
latest_tokens = []  # Variable global para mostrar en HTML

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
    </body>
    </html>
    """
    return render_template_string(html, tokens=latest_tokens)

def simple_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
