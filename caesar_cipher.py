from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homw(name=None):
        return render_template('index.html', name=name)

@app.route("/encode")
def encode(name=None):
        return render_template('encode.html', name=name)