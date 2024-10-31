from flask import Flask,render_template
import os

app = Flask(__name__, static_folder="static", template_folder=f"{os.getcwd()}/templates")

print(os.getcwd())

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")