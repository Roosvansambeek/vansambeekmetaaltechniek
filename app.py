from flask import Flask, render_template, url_for, request, jsonify
from email.message import EmailMessage
import ssl
import smtplib

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
    send_email(data)
    print(data)  # Log de ontvangen data
    return render_template('aanvraag.html', aanvraag=data)




def send_email(data):
  email_sender = "sambeekvanroos@gmail.com"
  email_password = 'gfdt unhv hrio clos'
  email_receiver = "sambeekvanroos@gmail.com"
  
  subject = '(aan)vraag'
  body = f"""
    Naam: {data['full-name']}
    Email: {data['email']}
    Telefoonnummer: {data['telefoonnummer']}
    Vraag/offerte aanvraag: {data['vraag']}
    """
  
  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email_receiver
  em['Subject'] = subject
  em.set_content(body)
  
  context = ssl.create_default_context()
  
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)