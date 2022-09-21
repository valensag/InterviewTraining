from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'valensagnin@gmail.com'
app.config['MAIL_PASSWORD'] = 'tzdmmgxquvjkavdv'
app.config['MAIL_DEFAULT_SENDER'] =  ('Valentina Salazar','valensagnin@gmail.com')
app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello Babeee', recipients=['zeatgomez@gmail.com'])
    msg.body = 'This is a test email sent from my flask app'
    
    with app.open_resource('luffy.jpeg') as luffy:
        msg.attach('luffy.jpeg', 'image/jpeg', luffy.read())
    mail.send(msg)

    return 'Message has been sent!'

@app.route('/bulk')
def bulk():
    users = [{'name':'Vale', 'email': 'zeatgomez@gmail.com'}]
    with mail.connect() as conn:
        for user in users:
            msg = Message('Bulk!', recipients=[user['email']])
            msg.body = 'Hey There!'
            conn.send(msg)


if __name__ == '__main__':
    app.run()
