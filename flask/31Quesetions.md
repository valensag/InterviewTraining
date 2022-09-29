# What is Flask?
Is a web development framework for Python, is based in Jinga2 foundation templates engine, open-source used to create Web applications using Python programming language. The default host is a localhost (127.0.0.1) and the default port is 5000

# How to add the mailing feature to the Flask Application?
Please check the file ```flask-mail.py``` to understand the configuration
```
pip install Flask-Mail
```
1. From flask and then import from flask_mail the Mail
2. Create an instance of the a flask app with ```app = Flask(__name__)```
3. Configure the variables to use with the Flask Config API:
    - MAIL_SERVER
    - MAIL_PORT
    - MAIL_USERNAME
    - MAIL_PASSWORD
    - MAIL_USE_SSL 
    - MAIL_DEFAULT_SENDER
    - MAIL_MAX_EMAILS
4. We need to import the Message Class and create an instance ```mail = Mail(app)```
5. Create a route to send the email. Use Message to define the message title and recipients, you also can use ```msg.body```to add some info inside de mail, even you can add some pics using ```msg.attach```. Finally you use the instanced variable mail to send the mail ```mail.send(msg)```.
```
@app.route('/') 
def index():
    msg = Message('Hello there', recipients['mail@mail.com'])
    msg.body = 'This is a test email sent from my flask app'
    with app.open_resource('luffy.jpeg') as luffy:
        msg.attach('luffy.jpeg', 'image/jpeg', luffy.read())
    mail.send(msg)
```
6. We always needs to add this to be able to run this app
```
if __name__ == '__main__':
    app.run()
```

# What is WSGI?
```Web Server Gateway Interface``` is a specification that describes how a web server communicates with a web application



