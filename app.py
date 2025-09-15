from flask import Flask, render_template, request
import os
import model  
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    dream_text = request.form.get("dream", "")
    mood = request.form.getlist("mood")
    emotion = request.form.getlist("emotion")

   
    result_text = model.analyze_dream(dream_text, mood, emotion)

    return render_template("result.html", result=result_text)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=False)
