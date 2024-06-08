from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html')

@app.route("/overons")
def overons():
  return render_template('overons.html')

@app.route("/werkzaamheden")
def werkzaamheden():
  return render_template('werkzaamheden.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)