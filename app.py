from re import DEBUG
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
  return "Hello,World"


if __name__ == "__main__":
  "I'm inside the script now"
  app.run(host='0.0.0.0', debug=True)
