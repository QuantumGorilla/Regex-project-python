# Filtrar textos que contengan el error de n seguida de b o n seguida de p y reemplazar por m en ambos casos
import re
words = ['abonbar', 'adormecer', 'Acalanbrar', 'Alanbrar', 'acanpar']
for word in words:
    e =  re.search('(\w*nb\w*)|(\w*np\w*)', word, flags=re.IGNORECASE)
    if e:
        print(words.index(e.group()))