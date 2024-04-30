from flask import Flask , render_template

def create_app():
    #create and configure the app
    app = Flask(__name__)

    #A simple page that says hello
    @app.route("/")
    def home (name= 'home'):
        return render_template('index.html', name=name)

    @app.route("/encode")
    def encode (name= 'encode'):
        return render_template('encode.html', name=name) 
    return app       