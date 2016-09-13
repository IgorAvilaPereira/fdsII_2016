import os
from flask import *
from werkzeug.utils import secure_filename
from simple_page import simple_page

# diretorio onde os arquivos serao armazenados
UPLOAD_FOLDER = './arquivos/'

# extensoes permitidas
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix='/simple_page')

# para usar sessoes e usar as mensagens flash
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# tamanho maximo dos arquivos (exemplo - no maximo 1 mb)
#app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Formulario sem o input file...')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        if file and allowed_file(file.filename):

            #print "Antes do Secure:"+file.filename
            filename = secure_filename(file.filename)
            print "Depois do Secute:"+filename

            # se quiser manter o nome original
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # se quiser colocar outro nome no arquivo
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], "igor."+ filename.rsplit('.', 1)[1]))

            flash('Upload realizado com sucesso')
            return redirect(url_for('upload_file'))
    return render_template('upload_file.html')

# ===========================================================================

# EXEMPLO AJAX

@app.route('/teste_ajax')
def index():
    return render_template("teste_ajax.html")

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    username = request.form['username']
    secret = request.form['secret']
    #return str(secret) + "eh muito ruim"
    #return jsonify(username = username, secret = secret)
    return "{\"employees\":[{\"firstName\":\"John\"}, {\"firstName\":\"Mifael\"} ]}"
# ===============================================================================


@app.before_request
def before_req():
    app.logger.debug('Isto ira ser executado antes da chamada da rota')

@app.route('/teste')
def home():
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')
    app.logger.debug('Executando a rota...')
    return "Oi!!!"
    #return g.target + '\n'

"""
def after_this_request(func):
    if not hasattr(g, 'call_after_request'):
        g.call_after_request = []
    g.call_after_request.append(func)
    return func
"""

@app.after_request
def per_request_callbacks(response):
    app.logger.debug("after lllll")
    """
    for func in getattr(g, 'call_after_request', ()):
        response = func(response)
    """
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()
