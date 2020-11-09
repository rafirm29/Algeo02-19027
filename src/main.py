import os
from flask import Flask, request, jsonify, flash, redirect, url_for, render_template, request
from flask import send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "secret key"

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'files')
# Make directory if "files" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/')
    '''
    if request.method == 'POST':
        # Mengecek apakah post request memiiki bagian file
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # Jika tidak select file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(request.url)
    return render_template("index.html")
    '''

@app.route('/search/', methods=['GET'])
def search():
    ### Pengolahan query ###
    str1 = request.args['q']
    str2 = str1.split()

    #results = []

    #for word in str1:
    #    results.append(word)
    
    return jsonify(str1)

@app.route('/perihal/', methods=['GET'])
def perihal():
    return render_template("perihal.html")

#app.secret_key = 'some secret key'
if __name__ == '__main__':
   app.run(debug = True)