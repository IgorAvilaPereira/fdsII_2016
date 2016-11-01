# desabilitar alguns warnings - extension AutoIndex
import warnings
from flask.exthook import ExtDeprecationWarning
warnings.simplefilter('ignore', ExtDeprecationWarning)

# link extensions http://flask.pocoo.org/extensions/
from flask import *

# extensao pdf....

# opcao1
# pip install reportlab
from reportlab.pdfgen import canvas

# opcao2 - bugs....
# pip install xhtml2pdf
# from xhtml2pdf import pisa

# opcao 3
# sudo pip install Flask-WeasyPrint
from flask_weasyprint import HTML, render_pdf

# minificar css e js
# http://flask-assets.readthedocs.io/en/latest/
# sudo pip install Flask-Assets
from flask_assets import Environment, Bundle

#email
# sudo pip install Flask-Mail
from flask_mail import *
# email: tadsfds2@gmail.com senha: mifael12345

# criptgrafia
# sudo pip install flask-bcrypt
from flask_bcrypt import Bcrypt

# admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# sudo pip install Flask-AutoIndex
import os.path
from flask import Flask

# depreciado
#from flask.ext.autoindex import AutoIndex
# atualizado
from flask_autoindex import AutoIndex


# aplicacao
app = Flask(__name__)
# index...
#AutoIndex(app, browse_root=os.path.curdir)

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# criptografia
bcrypt = Bcrypt(app)

# Flask and Flask-SQLAlchemy initialization here
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/flask_admin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)
# modelo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    def __init__(self, username = "", email = ""):
        self.username = username
        self.email = email
    def __repr__(self):
        return '<User %r>' % self.username
# admin
admin = Admin(app, name='Mauricio', template_mode='bootstrap3')
# definir qual modelo serah utilizado no admin
admin.add_view(ModelView(User, db.session))

# email..
mail = Mail()
app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'tadsfds2',
    MAIL_PASSWORD = 'mifael12345'
    )
mail.init_app(app)
# minificar
assets = Environment()
assets.init_app(app)

js = Bundle(
    'js/jquery-3.1.1.js',
    'js/script.js',
    filters='rjsmin',
    output='js/libs.js'
)
assets.register('js_libs', js)

"""
css = Bundle(
    'css/normalize.css',
    'css/main.css',
    filters='cssmin',
    output='css/min.css'
)
assets.register('css_all', css)
"""

# view de exemplo - flask_assets (minificar css e/ou js)
@app.route('/')
def hello_world():
    app.logger.debug('Renderizando o hello_world')
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')

    #criptografia
    pw_hash = bcrypt.generate_password_hash('hunter2')   
    # mensagem de debug
    app.logger.debug(str(pw_hash))
    bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True    

    msg = Message("Hello!!!", sender="tadsfds2@gmail.com", recipients=["ecomp.igorp@gmail.com"])
    #msg.body = "testing"
    msg.html = "<b>testing</b>"
    mail.send(msg)



    return render_template("index.html", mensagem = "Hello World")

# gerar pdf
@app.route('/pdf')
def pdf():
    import cStringIO
    output = cStringIO.StringIO()

    p = canvas.Canvas(output)
    # funciona tb
    #p.drawString(100, 100, render_template("hello_world.html", mensagem = "oi"))
    p.drawString(100, 100,"Hello World")
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()

    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename='pdf.pdf"
    response.mimetype = 'application/pdf'
    return response

"""
# gerar pdf
@app.route('/pdf2')
def convertHtmlToPdf():
    html = render_template("hello_world.html", mensagem = "Hello World")
    file = open('pdf2.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')
    file.seek(0)
    pdf = file.read()
    file.close()
    response = make_response(pdf)
    response.headers['Content-Disposition'] = "attachment; filename='pdf2.pdf"
    response.mimetype = 'application/pdf'
    return response
"""

@app.route('/pdf3')
def hello_pdf():
    html = render_template('hello.html', name="Monica....")
    return render_pdf(HTML(string=html))


if __name__ == "__main__":
    # para criar as tabelas 
    db.create_all() 
    # habilitar debug
    app.debug = True
    # rodar a aplicacao
    app.run()
