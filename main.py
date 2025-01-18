from flask import Flask,Blueprint


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask"


@app.route('/register')
def register():
    return "Registration Page"

@app.route('/login')
def login():
    return "Login Page"


app.run()