# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:09:49 2020

@author: Legion
"""
import re
import string
#from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def clean_file(name):
    file = open(name, 'r')
    f = file.readlines()
    
    new=[]
    for line in f:
        new.append(line)
        
    print(new)
    
    new_clean=[]
    for d in new:
        # Remove Unicode
        new_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
        # Remove Mentions
        new_test = re.sub(r'@\w+', '', new_test)
        # Lowercase the document
        new_test = new_test.lower()
        # Remove punctuations
        new_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', new_test)
        # Lowercase the numbers
        new_test = re.sub(r'[0-9]', '', new_test)
        # Remove the doubled space
        new_test = re.sub(r'\s{2,}', ' ', new_test)
        new_clean.append(new_test)
        
    print(new_clean)
    return new_clean
    
    