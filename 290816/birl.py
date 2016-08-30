# criacao de apps flask
from flask import Flask

# templates
from flask import render_template

# redirecionamento
from flask import redirect, url_for

# trabalhando com form
from flask import request

# trabalhando com session
from flask import session

app = Flask(__name__)

@app.route("/formulario")
def formulario():
    nome = ""
    senha = ""
    if 'nome' in session:
        nome =  session['nome']
    if 'senha' in session:
        senha = session['senha']
    return render_template("formulario.html", nome = nome, senha = senha)

@app.route("/recebe", methods=['POST'])
def recebe():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        session['nome'] = nome
        session['senha'] = senha
        return str(nome) + ":::::::::" + str(senha)
    else:
        return "Ta vindo nada inocente...."


@app.route('/tinder/<name>')
@app.route('/tinder')
def tinder(name=None):
    return render_template('tinder.html', name=name)

@app.route("/")
def index():
    return redirect(url_for("hello"))

@app.route("/hello")
def hello():
    x = "HELLO WORLD"
    vet = ['Igor', 'Bambam', 'felipefranco']
    return render_template("hello.html", mensagem = x, bambam = "felipefranco", frangos = vet)

@app.route("/ehhoradoshow")
@app.route("/trapeziodescendente")
def ehhoradoshow():
    return "Como eh que nao vai dah rapah!!!"


if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.debug = True
    app.run()
