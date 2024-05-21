from flask import Flask, render_template, request, flash
from app.encode import encode_message

def create_app():
    #create and configure the app
    app = Flask(__name__)
    app.config ['SECRET_KEY'] = 'kakakakakakkakakkakaa'

    #A simple page that says hello
    @app.route("/")
    def home (name='Home'):
        return render_template('index.html', name=name)

    @app.route("/encode",methods=('GET', 'POST'))
    def encode (name= 'encode'):
        if request.method == 'POST':
            try:
                cipher_key = int(request.form['cypher_key'])
            except:
                cypher_key = 0

            message = request.form['message']
            cipher_key = request.form['cipher_key']
            message = request.form['message']
        
            if not cipher_key == 0:
                flash('A chave é obrigatória...')
            elif not cipher_key:
                flash('a chave é obrigatória...')
            elif not message:
                flash('A mensagem é necessária...')
            else:
                flash("ENCODE")

        return render_template('encode.html', name=name)

    return app