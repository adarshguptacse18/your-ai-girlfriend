from flask import Flask, request, render_template, send_file, jsonify
from gemini import get_gemini_response
from speechToText import conver_to_audio
import json
# from app import AIGirlfriend
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tts", methods=["POST"])
def tts():
    messages = request.form.get("messages")
    messages = json.loads(messages)
    messages = get_gemini_response(messages)
    return jsonify({"message": messages})

@app.route("/getAudio", methods=["POST"])
def getAudio():
    text = request.form.get("message")
    id = conver_to_audio(text)
    return send_file(id, as_attachment=True)

    # return text
if __name__ == "__main__":
    app.run(debug=True)