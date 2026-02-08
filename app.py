from flask import Flask, render_template, request
from analysis.password import password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password_input = request.form["password"]
        score, scorestr, feedback = password(password_input)
        return render_template("index.html", password=password_input, score=score, scorestr=scorestr, feedback=feedback)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
