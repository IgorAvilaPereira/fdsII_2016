import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import string, time, math, random


UPLOAD_FOLDER = './static/arquivos'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

# Exemplo Ajax
# ====================================================
@app.route('/_add_numbers')
def add_numbers(a, b):
    #request.
    a = request.args.get('a', 0, type=int)
    print "===================="
    a = request.form['a']
    b = request.form['b']
    print "===================="
    #b = request.args.get('b', 0, type=int)
    return str(a)

@app.route('/ajax')
def index():
    return render_template('index.html')

# ====================================================

# Upload
# ====================================================
def uniqid(prefix='', more_entropy=False):
    m = time.time()
    uniqid = '%8x%05x' %(math.floor(m),(m-math.floor(m))*1000000)
    if more_entropy:
        valid_chars = list(set(string.hexdigits.lower()))
        entropy_string = ''
        for i in range(0,10,1):
            entropy_string += random.choice(valid_chars)
        uniqid = uniqid + entropy_string
    uniqid = prefix + uniqid
    return uniqid

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('Sem arquivos')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], uniqid() + "."+ file.filename.rsplit('.', 1)[1]))
            #return redirect(url_for('upload_file', filename=filename))
            return redirect("/")
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
# ====================================================

# Main
if __name__ == "__main__":
    app.run(debug=True)
