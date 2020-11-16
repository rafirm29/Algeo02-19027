# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:09:49 2020

@author: Legion
"""
import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#cleaning file
def clean_file(name):
    file = open(name, 'r', encoding="utf8")
    f = file.readlines()
    
    new=[]
    for line in f:
        newline = line.replace("\n", "")
        new.append(newline)
    new = ''.join(new)
    newtext = []
    newtext.append(new)
    
    new_clean=[]
    for d in newtext:
        # Menghilangkan Unicode
        new_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Memproses angka
        new_test = re.sub(r'[0-9]', '', new_test)
        # Menghilangkan kapital
        new_test = new_test.lower()
        # Menghilangkan @
        new_test = re.sub(r'@\w+', '', new_test)
        # Menghilangkan spasi ganda
        new_test = re.sub(r'\s{2,}', ' ', new_test)
        # Menghilangkan tanda baca
        new_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', new_test)
        new_clean.append(new_test)
    return new_clean
    
# stemming
def stem(kalimat):
    output = []
    for i in kalimat:
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        output = stemmer.stem(i)
    return(output)

# cleaning query
def cleanQuery(new):
    new_clean=[]
    # Menghilangkan Unicode
    new_test = re.sub(r'[^\x00-\x7F]+', ' ', new)
    # Menghilangkan spasi ganda
    new_test = re.sub(r'\s{2,}', ' ', new_test)    
    # Menghilangkan @
    new_test = re.sub(r'@\w+', '', new_test)
    # Menghilangkan kapital
    new_test = new_test.lower()
    # Menghilangkan tanda baca
    new_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', new_test)
    # Memproses angka
    new_test = re.sub(r'[0-9]', '', new_test)
    new_clean.append(new_test)
        
    return new_clean
