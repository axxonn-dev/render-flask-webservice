from flask import Flask, request, jsonify
import re
import os
app = Flask(__name__)

@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.get_json()
    text = data.get("text", "")
    tokens = simple_tokenize(text)
    return jsonify({"tokens": tokens})

def simple_tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
