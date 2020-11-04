# Filtrar textos que contengan el error de n seguida de b o n seguida de p y reemplazar por m en ambos casos
import re

def using_regular(word):
    e = re.search('(\w*nb\w*)|(\w*np\w*)', word, flags=re.IGNORECASE)
    if e:
        return e.group()

def fixed_list(errors):
    fixed = []
    for error in errors:
        if 'np' in error:
            fixed.append(error.replace('np', 'mp'))
        elif 'nb' in error:
            fixed.append(error.replace('nb', 'mb'))
    return fixed       

def sentence_error():
    sentence = input('Digite una oración: ')
    words = sentence.split(' ')
    errors = list()
    fixed = list()
    for word in words:
        errors.append(using_regular(word))
    errors[:] = (error for error in errors if type(error) == str) 
    fixed = fixed_list(errors)
    for i,j in zip(errors, fixed):
        print(i + ' = ' + j)
    
def list_error():
    words = list()
    while True:
        word = input('Digite una palabra: ')
        if word:
            words.append(word)
        else:
            break
    errors = list()
    fixed = list()
    for word in words:
        errors.append(using_regular(word))
    errors[:] = (error for error in errors if type(error) == str) 
    fixed = fixed_list(errors)
    for i,j in zip(errors, fixed):
        print(i + ' = ' + j)
    
def word_error():
    word = input('Digite una palabra: ')
    error = using_regular(word)   
    if 'np' in error:
        print(error + ' = ' + error.replace('np', 'mp'))
    elif 'nb' in error:
        print(error + ' = ' + error.replace('nb', 'mb'))
    
def file_error():
    name = input('Digite el nombre del archivo')
    file = open(name + '.txt')
    errors = []
    fixed = []
    for line in file:
        words = line.split(' ')
        for word in words:
            errors.append(using_regular(word))
    errors[:] = (error for error in errors if type(error) == str) 
    fixed = fixed_list(errors)
    for i,j in zip(errors, fixed):
        print(i + ' = ' + j)
    
print('Menu: \n' + '1. Error/es en una oración\n'+  '2. Error/es en una lista\n' +
      '3. Error en una palabra\n' + '4. Error/es en un archivo')
options = {'1': sentence_error, 
           '2': list_error, 
           '3': word_error, 
           '4': file_error}
argument = input('Digite un opción: ')
func = options.get(argument, 'Opción invalida')