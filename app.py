from flask import Flask, render_template, request
from analysis.password import password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    score_str = None
    feedback = None
    password_input = ""
    
    if request.method == "POST":
        password_input = request.form.get("password", "")
        score, score_str, feedback = password(password_input)
    
    return render_template("index.html", score=score, score_str=score_str, feedback=feedback, password_input=password_input)

if __name__ == "__main__":
    app.run(debug=True)
