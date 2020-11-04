# Filtrar textos que contengan el error de n seguida de b o n seguida de p y reemplazar por m en ambos casos
import re as regex

def using_regular(input):
    e = regex.search('(\w*nb\w*)|(\w*np\w*)', input, flags=regex.IGNORECASE)
    if e:
        return e.group()
        

def sentence_error():
    sentence = 'Input some shit right here, motherfucker'
    words = sentence.split(' ')
    errors = list()
    for word in words:
        errors.append(using_regular(word))
    
def list_error():
    words = list()
    errors = list()
    for word in words:
        errors.append(using_regular(word))
    
    
def word_error():
    word = 'Input'
    error = using_regular(word)   
    
def file_error():
    name = 'input file name'
    file = open(name + '.txt')
    errors = []
    for line in file:
        words = line.split(' ')
        for word in words:
            errors = using_regular(word)