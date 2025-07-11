from flask import Flask, request, jsonify, render_template_string
import re
import os

app = Flask(__name__)

@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.get_json()
    text = data.get("text", "")
    tokens = simple_tokenize(text)
    return render_tokens_html(tokens)

def simple_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def render_tokens_html(tokens):
    html = """
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>Tokens</title></head>
    <body>
        <h2>Tokens:</h2>
        <ul>
            {% for token in tokens %}
            <li>{{ token }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(html, tokens=tokens)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)