from re import DEBUG
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Support Analyst',
    'location': 'Harare, Zimbabwe',
    'salary': 'ZiG. 10,00,000'
}, {
    'id': 3,
    'title': 'Accountant Analyst',
    'location': 'Gweru, Zimbabwe',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 4,
    'title': 'Database Engineer',
    'location': 'Gokwe, Zimbabwe',
    'salary': 'Rs. 10,00,000'
}]


@app.route('/')
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='Easytouch')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  "I'm inside the script now"
  app.run(host='0.0.0.0', debug=True)
