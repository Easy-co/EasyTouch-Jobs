from re import DEBUG
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":
  "I'm inside the script now"
  app.run(host='0.0.0.0', debug=True)
