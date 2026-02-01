from flask import Flask
from analysis.password import password

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
