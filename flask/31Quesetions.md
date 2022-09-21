# What is Flask?
Is a web development framework for Python, is based in Jinga2 foundation templates engine, open-source you can get the development versions in a github url and running the command 
``` 
cd flask && python3 setup.py develop
```
# How to add the mailing feature to the Flask Application?
Please check the file ```flask-mail.py``` to understand the configuration
```
pip install Flask-Mail
```
Once installed, then we need to use Flask Config API to configure 
- MAIL_SERVER
- MAIL_PORT
- MAIL_USERNAME
- MAIL_PASSWORD
- MAIL_USE_SSL 
- MAIL_DEFAULT_SENDER
- MAIL_MAX_EMAILS
Then we need to import Message Class, instantiate it and form a message object before sending the mail by using the mail.send() method.