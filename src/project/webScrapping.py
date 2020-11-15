import requests
from bs4 import BeautifulSoup
import re
import string

from textprocessing import inputKata, gabungarray, listToString, removeduplicatex, jumlahKata
from clean_txt import clean_file, stem
from cosinesim import sim

def webScrapping(web, namafile):
    documents = []

    r = requests.get(web)

    soup = BeautifulSoup(r.content, 'html.parser')
    sen = []
    for i in soup.find('div', {'class':'read__content'}).find_all('p'):
        sen.append(i.text)
    documents.append(' '.join(sen))
    # namafile = str(input("Masukkan nama file yang ingin ditulis (dalam txt): "))
    file1 = open("../test/" + namafile + ".txt","w+", encoding="utf8")
    file1.writelines(documents)
    file1.close()