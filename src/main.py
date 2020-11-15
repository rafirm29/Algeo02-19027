import os
import math
import sys
sys.path.insert(1, 'project')
from textprocessing import inputKata, gabungarray, listToString, removeduplicatex, jumlahKata
from clean_txt import clean_file, stem, cleanQuery
from cosinesim import sim
from flask import Flask, request, jsonify, flash, redirect, url_for, render_template, request
from flask import send_from_directory
from werkzeug.utils import secure_filename
from webScrapping import webScrapping

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, '../test')
# Make directory if "test" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__, static_folder="../test")

app.secret_key = "secret key"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def sort(array): # Sorting berdasarkan similarity
    arrayoftuple = array
    for i in range(len(arrayoftuple)):  
        
        maxtemp = i 
        for j in range(i+1, len(arrayoftuple)): 
            if arrayoftuple[maxtemp][1] < arrayoftuple[j][1]: 
                maxtemp = j        
        arrayoftuple[i], arrayoftuple[maxtemp] = arrayoftuple[maxtemp], arrayoftuple[i]
    return arrayoftuple

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def upload():
    if request.method == 'POST':
        if request.form['button'] == '  Add  ':
            link = request.form['link']
            title = request.form['title']
            webScrapping(link, title)
            # return jsonify(link)
        elif request.form['button'] == 'Upload':
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

@app.route('/search/', methods=['GET'])
def search():
    query = request.args['q'] # Input query

    ###############################
    ##### Document Processing #####
    ###############################

    onlyfiles = next(os.walk('../test'))[2] #open semua file pada directory
    search = query #input query searching
    arr = [] 
    sorted =[]
    arrQuery = cleanQuery(search)
    stemQuery = stem(arrQuery)
    listToStringQ = listToString(stemQuery)
    searchtoarray = inputKata(listToStringQ) #membuat input query menjadi array of words

    for files in onlyfiles:
        
        filename = "../test/" + files
        clean = clean_file(filename) #cleaning
        stemfile = stem(clean) #stemming
        arraytostring = listToString(stemfile) #mengubah array of kalimat menjadi string
        arrayfile = inputKata(arraytostring) #mengubah string menjadi array of word dari file yang dibaca
        searchtoarray = gabungarray(searchtoarray,arrayfile) #concate dengan dokumen yg sedang dibaca

    removeVec = removeduplicatex(searchtoarray) #menghapus kata yang sama

    for files in onlyfiles:
        
        filename = "../test/" + files
        clean = clean_file(filename)
        stemfile = stem(clean)
        arraytostring = listToString(stemfile)
        arrayfile = inputKata(arraytostring)
        fp= open(filename, 'r', encoding="utf8")
        c = listToString(fp)
        count = 0
        for word in c.split():
            count += 1
        arrQuery = cleanQuery(search)
        stemQuery = stem(arrQuery)
        listToStringQ = listToString(stemQuery)
        arrQuery = inputKata(listToStringQ) #membuat input query menjadi array of words
        sumofword = jumlahKata(arrQuery, removeVec) #membuat array vectorizer pada query
        sumofwordDoc = jumlahKata(arrayfile, removeVec) #membuat array vectorizer pada file yang dibaca
        cosinesimilarity = sim(sumofword, sumofwordDoc) #calculate sim

        docs = files
        N = cosinesimilarity * 100
        firstsen = c.split(".")
        # print("Kalimat pertama : " + firstsen[0] + '.')
        arr.append((docs,N)) #membuat tupple untuk menyimpan (namafile,sim)
        sorted.append((docs,N,firstsen[0] + ".", count)) #membuat tupple untuk menyimpan (namafile,sim)

    tempresult = sort(sorted)
    Qresult = []
    i = 1
    for q in tempresult:
        Qresult.append((i, q[0], str('{0:.2f}'.format(q[1])) + " %", q[2], q[3]))
        i += 1


    ##########################    
    ##### Tampil Matriks #####
    ##########################  

    number = len(Qresult) + 1

    # tampil matriks
    arrQuery = cleanQuery(search)
    stemQuery = stem(arrQuery)
    listToStringQ = listToString(stemQuery)
    searchtoarray = inputKata(listToStringQ)
    row = removeduplicatex(searchtoarray)
    table = [[0 for j in range(number+1)]for i in range(len(row)+1)]
    for i in range(len(row)+1):
        for j in range(number+1):
            if (j==0 and i != 0 ): #mengisi vektor dokumen
                table[i][j]=str(removeVec[i-1]) + "  "
            elif(i==0 and j==1): #menulis 'query' pada kolom 0 baris 1
                table[i][j] = 'query  ' 
            elif (i==0 and j==0):
                table[i][j] = 'term  '
            elif ( j!=0 and i==0):
                table[i][j]=str(arr[j-2][0]) + "  " #menulis nama dokumen
            elif(j==1 and i!=0): #menulis vektor query
                table[i][j]=sumofword[i-1]    

    kolom = 2
    for files in onlyfiles:
        if (kolom>1):
            filename = "../test/" + files
            clean = clean_file(filename)
            stemfile = stem(clean)
            arraytostring = listToString(stemfile)
            arrayfile = inputKata(arraytostring)

            arrQuery = inputKata(search) #membuat input query menjadi array of words
            sumofwordDoc = jumlahKata(arrayfile, removeVec) #membuat array vectorizer pada file yang dibaca
        for i in range(len(row)+1):
            if (kolom!=1 and i!=0): #menulis vektor setiap dokumen
                table[i][kolom]=sumofwordDoc[i-1]
        kolom += 1

    del table[0]
    rowlength = len(table[0])

    return render_template("search.html", result=Qresult, thead=arr, tbody=table, rowlength=rowlength)

@app.route('/perihal/', methods=['GET'])
def perihal():
    return render_template("perihal.html")

#app.secret_key = 'some secret key'
if __name__ == '__main__':
   app.run(debug = True)
