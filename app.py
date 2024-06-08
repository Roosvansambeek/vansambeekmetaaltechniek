from flask import Flask, render_template, url_for, request, jsonify

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

@app.route("/contact")
def contact():
  return render_template('contact.html')


@app.route("/contact/verstuurd", methods=["POST"])
def vraag_verstuurd():
    data = request.form
    print(data)  # Log de ontvangen data
    return render_template('aanvraag.html', aanvraag=data)

  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)