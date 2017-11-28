#main.py

# [START imports]
import logging, traceback
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from email_info import get_info
# [END imports]

# [START create_app]
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')
email_username, email_password = get_info()
app.config['MAIL_USERNAME'] = email_username
app.config['MAIL_PASSWORD'] = email_password
mail = Mail(app)
# [END create_app]

# [START routing]


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/demo')
def demo():
    return render_template("demo.html")


@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/blog/swe')
@app.route('/blog/swe/<week>')
def swe(week=None):
    return render_template('blog/swe/template.html')



@app.route('/send_message', methods=['POST'])
def send_message():
    if email_username is None or email_password is None:
        return "Something went wrong. Please try again later or send an email to thienqvo@gmail.com!"

    contact_name = request.form['contactName']
    contact_subject = request.form['contactSubject']
    contact_message = "Received from: {0}\n{1}".format(request.form['contactEmail'], request.form['contactMessage'])

    if contact_subject is None or contact_subject == "":
        contact_subject = "Message sent from thienmint.com"

    msg = Message(subject=contact_subject,
                  body=contact_message,
                  sender=(contact_name, email_username),
                  recipients=["thienqvo@gmail.com"])
    try:
        mail.send(msg)
    except Exception as e:
        logging.error(traceback.format_exc())
        return "Couldn't send email. Please try again later or send an email to thienqvo@gmail.com!"

    return "OK"


@app.route('/send_message', methods=['GET', 'PUT', 'DELETE'])
def redirect_contact():
    return redirect(url_for('home', _anchor='contact'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html")
# [END routing]


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
