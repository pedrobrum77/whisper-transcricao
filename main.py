from flask import Flask, request, render_template
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/", methods=["GET", "POST"])
def index():
    transcription = ""
    if request.method == "POST":
        audio = request.files["audio"]
        path = os.path.join("temp", audio.filename)
        audio.save(path)
        result = model.transcribe(path, language="pt")
        transcription = result["text"]
        os.remove(path)
    return render_template("index.html", transcription=transcription)

if __name__ == "__main__":
    app.run(debug=True)
