import requests
from bs4 import BeautifulSoup
import re
import string

from textprocessing import inputKata, gabungarray, listToString, removeduplicatex, jumlahKata
from clean_txt import clean_file, stem
from cosinesim import sim

def webScrapping(web):
    documents = []

    r = requests.get(web)

    soup = BeautifulSoup(r.content, 'html.parser')
    sen = []
    for i in soup.find('div', {'class':'read__content'}).find_all('p'):
        sen.append(i.text)
    documents.append(' '.join(sen))
    namafile = str(input("Masukkan nama file yang ingin ditulis (dalam txt): "))
    file1 = open("C:/Users/Haikal/Documents/Kampus/Algeo/Tubes2/Algeo02-19027/src/test/" + namafile + ".txt","w+")
    file1.writelines(documents)
    file1.close() 


b = str(input())
webScrapping(b)