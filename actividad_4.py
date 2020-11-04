# Filtrar textos que contengan el error de n seguida de b o n seguida de p y reemplazar por m en ambos casos
import re
import sys

def using_regular(word):
    e = re.search('(\w*[nN][bB]\w*)|(\w*[nN][pP]\w*)', word, flags=re.IGNORECASE)
    if e:
        return e.group()

def fixed_list(errors, isFile):
    errors[:] = (error for error in errors if type(error) == str)
    if len(errors) > 0:
        fixed = []
        for error in errors:
            if 'np' in error:
                fixed.append(error.replace('np', 'mp'))
            elif 'nb' in error:
                fixed.append(error.replace('nb', 'mb'))
            elif 'nP' in error:
                fixed.append(error.replace('nP', 'mP'))
            elif 'Np' in error:
                fixed.append(error.replace('Np', 'Mp'))
            elif 'NP' in error:
                fixed.append(error.replace('NP', 'MP'))
            elif 'nB' in error:
                fixed.append(error.replace('nB', 'mB'))
            elif 'Nb' in error:
                fixed.append(error.replace('Nb', 'Mb'))
            elif 'NB' in error:
                fixed.append(error.replace('NB', 'MB'))
        for i,j in zip(errors, fixed):
            print(i + ' = ' + j)
        if isFile:
            return fixed
    else:
        print('No hubo error/es.')

def sentence_error():
    sentence = input('Digite una oración: ')
    words = sentence.split(' ')
    errors = list()
    fixed = list()
    for word in words:
        errors.append(using_regular(word))
    fixed_list(errors, False)    
    
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
    fixed_list(errors, False)
    
def word_error():
    word = input('Digite una palabra: ')
    error = using_regular(word)
    if error is not None:
        if 'np' in error:
            print(error + ' = ' + error.replace('np', 'mp'))
        elif 'nb' in error:
            print(error + ' = ' + error.replace('nb', 'mb'))
        elif 'nP' in error:
            print(error + ' = ' + error.replace('nP', 'mP'))
        elif 'Np' in error:
            print(error + ' = ' + error.replace('Np', 'Mp'))
        elif 'NP' in error:
            print(error + ' = ' + error.replace('NP', 'MP'))
        elif 'nB' in error:
            print(error + ' = ' + error.replace('nB', 'mB'))
        elif 'Nb' in error:
            print(error + ' = ' + error.replace('Nb', 'Mb'))
        elif 'NB' in error:
            print(error + ' = ' + error.replace('NB', 'MB'))
    else:
        print('No hay error.')

def punctuation(word):
    if ',' in word:
        real_word = word.split(',')
        real_word[1] = ',' 
        return real_word
    elif '.' in word:
        real_word = word.split('.')
        real_word[1] = '.' 
        return real_word
    elif '\n' in word:
        real_word = word.split('\n')
        real_word[1] = '\n'
        return real_word 
    elif ';' in word:
        real_word = word.split(';')
        real_word[1] = ';'
        return real_word 
    elif '?' in word:
        real_word = word.split('?')
        real_word[1] = '?'
        return real_word
    elif '!' in word:
        real_word = word.split('!')
        real_word[1] = '\n'
        return real_word
    else:
        return word

def file_error():
    name = input('Digite el nombre del archivo: ')
    found = False
    try:
        errors_file = open(name + '.txt')
    except IOError:
        print('No se pudo abrir el archivo.')
        sys.exit()
    real_errors = []
    errors = []
    fixed = []
    for line in errors_file:
        words = line.split(' ')
        for word in words:
            errors.append(using_regular(word))
    fixed = fixed_list(errors, True)
    errors_file.seek(0,0)
    fixed_file = open('fixed.txt', 'w+')
    errors[:] = (error for error in errors if type(error) == str)
    for line in errors_file: 
        words = line.split(' ')
        row = ''
        for word in words:
            real_word = punctuation(word)
            if real_word[0] in errors:
                fixed_word = fixed[errors.index(real_word[0])]
                found = True
            elif real_word in errors:
                fixed_word = fixed[errors.index(real_word)]
                found = True
            if found:
                if '\n' in word:
                    row += ' ' + fixed_word + real_word[1] + '\n'
                elif type(real_word) == list:
                    row += ' ' + fixed_word + real_word[1]
                else:
                    row += ' ' + fixed_word
                found = False
            else:
                row += ' ' + word
        fixed_file.write(row)
    errors_file.close()
    fixed_file.close()
    
print('Menu: \n' + '1. Error/es en una oración\n'+  '2. Error/es en una lista\n' +
      '3. Error en una palabra\n' + '4. Error/es en un archivo')
options = {'1': sentence_error, 
           '2': list_error, 
           '3': word_error, 
           '4': file_error}
argument = input('Digite un opción: ')
func = options.get(argument, lambda: 'Opción invalida')
if int(argument) >= 1 and int(argument) <= 6:
    func()
else:
    print(func())