# What is Flask?
Is a web development framework for Python, is based in Jinga2 foundation templates engine, open-source used to create Web applications using Python programming language. 

Flask is called a ```microframework```because Flask only provides core features suck as request, routing and blueprints. For other features such as ORM and forms we need to make use of ```Flask-Extensions```

Some of the benefirs of using Flask framework are:
- It has an inbuilt development server.
- It has vast third-party extensions.
- It has a tiny API and can be quickly learned by a web developer.
- It is WSGI compliant.
- It supports Unicode.

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
```py
@app.route('/') 
def index():
    msg = Message('Hello there', recipients['mail@mail.com'])
    msg.body = 'This is a test email sent from my flask app'
    with app.open_resource('luffy.jpeg') as luffy:
        msg.attach('luffy.jpeg', 'image/jpeg', luffy.read())
    mail.send(msg)
```
6. We always needs to add this to be able to run this app
```py
if __name__ == '__main__':
    app.run()
```

# What is WSGI?
```Web Server Gateway Interface``` is a specification that describes how a web server communicates with a web application

# What is the default host and port of Flask and how to change it?
The default host is a localhost (127.0.0.1) and the default port is 5000, to change it we need to pass the values to host and port parameters while calling run method on the app.

```py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

# What is a Ajax application and how to create it?
Ajax's primary advantage is it's ability to ```improve performance``` and usability for web applications. Ajax allows applications to render with no data. This reduces server traffic and web developers can reduce the time taken to respond on both sides of the request. 

In modern browsers we are not longer using ajax, now we use ``fetch()`` that is a built-in JavaScript solution to making requests from a page. You can make your HTML page dynamic, by changing data without reloading the entire page. Instead of submitting a HTML <FORM> 

    To create an Ajax application we can use Flask-Sijax, an extension that uses Python/JQuery, once configured and initialized, it enables the use of @flask_sijax decorator, which we can use for making Ajax aware of the views in a Flask App.


# How to get query String in Flask?
We can get the argument's value using the ```request object``` in Flask. We can use the browser to navigate with the request parameter.
```py
from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route("/")
def index():
val = request.args.get("var") 
 
return "Hello, World! {}".format(val)
 
if __name__=="__main__":
app.run(host="0.0.0.0", port=8080)
```

# How to get the user agent in Flask?
We can use the ```request objetct``` to get the User-Agent in Flask

```py
from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route("/")
def index():
    val = request.args.get("var")
    user_agent = request.headers.get('User-Agent')   
 
    response = """
    &lt;p&gt;
    Hello, World! {}
    &lt;br/&gt;
    You are accessing this app with {}
    &lt;/p&gt;
    """.format(val, user_agent)    
return response
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
```

# How to use url_for in the Flask application?
Flask's url_for function helps in ```creating dynamic routes```. We can make use of url_for in the Flask ```templates```. We can call the view function with parameters and values to generate URLs

    Syntax: url_for('name of the function of the route','parameters (if required)')

```Example 1:```
## Flask server side
```py
@app.route('/<variable>/add', methods=['GET', 'POST'])
def add(variable):

@app.route('/<variable>/remove', methods=['GET', 'POST'])
def remove(variable):
```
## Flask tempalte side
```py
url_for('add', variable=foo)
url_for('remove', variable=foo)
```

Without ```url_for```, if there is a change in the root URL of your app then you have to change it in every page where the link is present.

```Example 2:```

## Flask server side     
```py
@app.route('/questions/<int:question_id>')    #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def find_question(question_id):  
    return ('you asked for question{0}'.format(question_id))
```

## Flask template side
```html
<a href = {{ url_for('find_question' ,question_id=1) }}>Question 1</a>
```

```Example 3:```
## Flask server side:
```py
@app.route(“/blog/post/<string:post_id>”)
def get_post_id(post_id):
    return post_id
```

## Flask template side:
```html
<a href=”{{ url_for(‘get_post_id’, post_id=post.id}}”>{{post.title}}<a>
```


# How to create an Admin interface in Flask?
We can create it using the ```Flask-Admin``` extension. It heps in ```grouping individual views together in classes```. Each web page you see on the frontend, represents a method on a class that has explicity been added to the interface. These view classes are specially helpul when they are tied to particular database models, because they let you group together all of the usual Create, Read, Update, Delete ```(CRUD)``` view logit into a single, self-contained class for each of your models.


# How to integrate Twitter or similar API with the Flask Application?
We can use the Flask extension ```Flask-Social```. It helps in authenticating users from Twitter and other platforms or accounts such as Facebook and google, we also need to use the ```Flask-Security```extension. We need to install individual API libraries in Python and also get consumer and secret keys by registering the Flask app on the external account providers.

# Is the SQLite database built-in Flask?
SQLite is in-built with Python. To use the database in Flask, we need not install any additional Flask-Extension. Inside the view, we can import SQLite and write SQL queries for interacting with the database. However, generally make use of ```Flask-SQLAlchemy```, which eliminates the need to write complex SQL queries and is an ORM to interact with the SQLite database.

# What do you mean by template engines in the Flask framework?
A template is a file that contains two types of data, ```static``` and ```dynamic```. Dynamic data in a template is populated during run time. Flask makes use of ```Jinja2 template engine``` to let developers create HTML templates with placeholders for dynamic data. These placeholders can be filled during run time by using Flask’s ```render_template``` method with required parameters and values.


# How to test Flask Applications?
Flask provides utilities for testing an app. We can use ```pytest``` framework to set up and run our tests. Writing unit test for your applications lets you check the code you wrote works the way you expect. Flask provides a ```test client``` that simulates requests to the app and returns the response data.

# What is the difference between Django and Flask? Why should one choose Flask?
Django is also a web development framework created in the Python programming language. It is a full-featured web application framework with a lot of features that are built into it, such as an Admin backend, and an ORM with migration capability. It is a little bit older and more mature.

Flask is better for quick development use cases and is perfect for prototyping. Django has inspired even some Flask extensions that are written. Flask is more suitable for developing lightweight web applications that do not require a large codebase. It is apt for developing microservices or serverless applications.

Flask is easy to learn and has fewer API’s when compared to Django. As the industry is following the trends towards microservices served as part of containers, it is excellent to keep Flask in your web development toolkit.

# Describe the features of Forms extension for Flask
Forms in Flask can be implemented by using an extension called ```Flask-WTF```. Flask-WTF is created by integrating Flask with ```WTForms```. WTForms is a python-based form rendering and validation library. It supports data validation, internationalization, and CSRF protection.

Flask-WTF also provides reCAPTCHA support along with file uploads when tied with Flask-Uploads. You also can handle JavaScript requests, and customize the error response.

# How to use a session in Flask?
We can use the ```Flask-Session```that supports Server-side Session to your application. 
- The session is the ```time``` between the client logs in to the server and logs out of the server.
- The data that is required to be saved in the Session is stored in a ```temporary directory``` on the server. 
- The data in the Session is stored on the ```top of cookies```. Each client will have their own sessions where their own data will be stored in their session.

Whenever we want to save some data between requests, then we make use of session objects in Flask. We can set and get data from the session object, as shown below.

```
pip install Flask-Session
```

The First line (session) from the flask is in such a way that each of us as a user gets our own version of the session.
```py
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
```

- **SESSION_PERMANENT** = False –  So this session has a default time limit of some number of minutes or hours or days after which it will expire.
- **SESSION_TYPE** = “filesystem” –   It will store in the hard drive (these files are stored under a /flask_session folder in your config directory.) or any online ide account, and it is an alternative to using a Database or something else like that.

```py
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
```
## Now let's try to remember a User after login
So we will start making two basic pages and their route called index.html and login.html

- **login.html** contains a form in which the user can fill their name and submit 
- **index.html** is the main page 
```py
@app.route("/")
def index():
    return render_template('index.html')
 
 
@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")
```
- We need to record the username in the session when they submit the form
- And we are using a dictionary in python where “name” is the key = request.form.get(“name”) is a value

```py
@app.route("/login", methods=["POST", "GET"])
def login():
  # if form is submited
    if request.method == "POST":
        # record the user name
        session["name"] = request.form.get("name")
        # redirect to the main page
        return redirect("/")
    return render_template("login.html")
```

- After storing the user name we need to check whenever user lands on the index page that any session with that user name exists or not.
- If the user name doesn’t exist then redirect to the login page.

```py
@app.route("/")
def index():
  # check if the users exist or not
    if not session.get("name"):
        # if not there in the session then redirect to the login page
        return redirect("/login")
    return render_template('index.html')
```
- After successfully remember the user we also need a way to logout the users.
- So whenever the user clicks logout change the user value to none and redirect them to the index page.

```py
@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
```

## index.html
We can also use session.name to excess the value from the session.
```js
{% extends "layout.html" %}
 
{% block y %}
 
   {% if session.name %}
      You are Register {{ session.name }} <a href="/logout">logout</a>.
   {% else %}
      You are not Register. <a href="/login">login</a>.
   {% endif %}
 
{% endblock %}

```

## login.html
```js
{% extends "layout.html" %}
 
{% block y %}
 
   <h1> REGISTER </h1>
 
   <form action="/login" method="POST">
      <input placeholder="Name" autocomplete="off" type="text" name="name">
      <input type="submit" name="Register">
   </form>
 
{% endblock %}
```

## logout.html
```html
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta name="viewport" content="initial-scale=1, width=device-width">
		<title> flask </title>
	</head>
	<body>
		{% block y %}{% endblock %}
	</body>
</html>

```

```Example 2:```

```py
from flask import Flask, session
 
app = Flask(__name__)
 
@app.route('/use_session')
def use_session()
    if 'song' not in session:
        session['songs'] = {'title': 'Tapestry', 'singer': 'Bruno Major'}
 
    return session.get('songs')
 
@app.route('/delete_session')
def delete_session()
    session.pop('song', None)
    return "removed song from session"
```

# What is the g object in Flask? How does it differ from the session object?
Flask’s g object is used as a global namespace for holding any data during the application context. g object is not appropriate for storing the data between requests. The letter g, in a sense, stands for global.

In situations, when you need to keep global variables during an application context, then rather than creating your global variable, it is best to use the g object as each request in Flask has a separate g object. Flask’s g object saves us from accidental modifications of self-defined global variables.

Occasionally you might find a situation in which using a global variable is a perfectly reasonable solution to a problem. However, in a Flask app, your code is likely to end up running in an environment with multiple requests being handled at the same time. If you used a normal global variable, one request might modify the global variable and interfere with another request that happens to be executing simultaneously. To avoid that, Flask provides this g object to which you can attach such variables. Each request gets a different g object, so simultaneous requests can't interfere with each other, but you still have the same convenience as a global variable.

# What is the application context in Flask?
Response and Request cycle
1. A cient make a request to the Flask server
2. The flask server make a few objects available to the view function that will handle it. Flask use ```Context```to pass the extra args to make the objects global accesibles within a thread without interfering each other.

There are 2 types of **Context** in flask:
## Application context
- current_app: Is an instance of the app
- g: Is an object that the app can use to temporary storage during the handling of a request and this variable is reset with each request.

## Request context
- request: Actual request contact and it encaptusulate the context of an HTTP request sent by the client
- session: Is a Dictionary that the application can use to store values that are remembered between the request.

Flask activates the application and request contacts before dispatching a request to the app and removes them off to the request is handled. when the app context is pushed ```app_context.push()``` the **current_app** and **g** avariable become available to the tread likewise when the ```request_context.push()``` is pushed, the requests and sessions become available.

When the app already recived the request from the client, it needs to find out what view function to invoke the service this request. For this Flask look to the ```Application url map``` which contains a map of url to the view functions.
```py
from flask import app
app.url_map
```

## Request object
request context => request: Have all the information that the client provide in the request
**Methods:**
- get_date: return data from the request body
- get_json: return a python dictionary with a parsed json includad in the body request
- is_secure: true or false if the secure connection is good

**Variables:**
- endpoint: handling the request, flask use the name of the view
- method: HTTP method (GET, POST)
- host: Port nomber
- URL: complete url (base_url)
- environ: environment dictionary with the request
**Request Hooks:**
- before_request
- before_first_request
- after_request
- teardown_request

When flask invoke the view function it expect to have a HTTP response. The status code is very important here.
**Methods:**
- set_cookie
- dekete_cookie
- set_data
- get_data
**Variables:**
- status_code
- headers
- content lenght
- content_type

## Redirect
Gives a url to navigate not a page or string

In conclusion...
The application context in Flask relates to the idea of a complete request/response cycle. It keeps a track of application-level data during a request of a CLI command. We make use of g and current_app proxies to achieve the same.

There are situations when it is difficult to directrly import the Flask app, such as in the case of a Flask extension or a Blueprint. Moreover, introducing applications may raise the problem of circular imports

Flask pushes the application context with each request. Therefore, during a request, functions have access to g and curent_app to ovecome the problem highlighted above.

# In what ways can you connect to a database in Flask?
Flask works with most of the RDBMSs, such as PostgreSQL, SQLite, and MySQL. However, to connect with databases, we must make use of the Flask-SQLAlchemy extension. SQLAlchemy is basically a bridge between Python and a SQL database

It makes database interaction and management easy during development without the need to write raw SQL queries. Moreover, raw SQL queries are prone to SQL injection attacks. For working with No-SQL data stores such as MongoDB, we can make use of the Flask-MongoEngine extension.

```
pip install flask-sqlalchemy
```
You’ll connect your Flask app to an existing SQL database. Connecting will require your own database username and database password, unless using SQLite.

```py
"""
    test a SQLite database connection locally
    assumes database file is in same location
    as this .py file
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'sockmarket.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)
```

# How to create a RESTful application in Flask?
We can use the extensions listed below
- Flask-API
- Flask-RESTful
- Flask-RESTX
- Connexion

# How to debug a Flask Application?
Flask comes with a development server, and the development server has a Debug Mode. The Debug mode can be set to true when we call the run method of the Flask Application object.

```py
from flask import Flask 
app = Flask(__name__)
app.run(host='127.0.0.1', debug=True)
```

Further, we can make use of the Flask-DebugToolbar extension for easy debugging in the browser. We can also make use of Python’s pdb module and the debugging statement import pdb;pdb.set_trace() to support the debugging process.

# What type of Applications can we create with Flask?
With Flask, we can create almost all types of web applications. We can create Single Page Application, RESTful API based Applications, SAS applications, Small to medium size websites, static websites, Microservices, and serverless apps.

Flask is so versatile and flexible as it can be integrated with other technologies very quickly to achieve the same. For example, Flask can be combined with the NodeJS serverless, AWS lambda, and similar other third party services to build new-age systems.
