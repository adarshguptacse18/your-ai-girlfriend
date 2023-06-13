from flask import Flask, request, render_template, send_file, jsonify
import requests
import uuid
from speechToText import conver_to_audio

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tts", methods=["POST"])
def tts():
    text = request.form.get("text")
    
    return jsonify({"message": text})

@app.route("/getAudio", methods=["POST"])
def getAudio():
    text = request.form.get("message")
    # id = conver_to_audio(text)
    id = "1e17748c-bee1-4db2-822c-15a37b199f0f.mp3";
    return send_file(id, as_attachment=True)

    # return text
if __name__ == "__main__":
    app.run(debug=True)