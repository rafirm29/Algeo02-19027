from clean_txt import clean_file
from stem_file import stem


#factory = StemmerFactory()
#stemmer = factory.create_stemmer()

#sentence = "perekonomian indonesia sedang dalam pertumbuhan yang membanggakan"
# = stemmer.stem(sentence)

#print(output)

#buat nyoba
files = str(input("masukkann nama file: "))    
a= clean_file(files)
stem(a)