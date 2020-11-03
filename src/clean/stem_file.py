
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def stem(kalimat):
    output =[]
    for i in kalimat:
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        output = stemmer.stem(i)
    print(output)
