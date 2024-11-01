from flask import Flask,render_template
import os

app = Flask(__name__, static_folder=f"{os.getcwd()}/static", template_folder=f"{os.getcwd()}/templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
