from flask import Flask, render_template, request
from analysis.password import password

app = Flask(__name__)
# Ensure the Flask CLI picks up development/debug mode when importing this module.
# Setting `ENV` to 'development' enables debug-related behavior when using `flask run`.
app.config.update(ENV="development", DEBUG=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password_input = request.form["password"]
        score, scorestr, feedback, color = password(password_input)
        return render_template("index.html", password=password_input, score=score, scorestr=scorestr, feedback=feedback, color=color)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
