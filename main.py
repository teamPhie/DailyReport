from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/test')
def test():
    return "Helllo!!!!!"


app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8080)
