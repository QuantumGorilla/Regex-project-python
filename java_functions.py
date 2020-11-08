# Determinar que los parámetros que pasan por value o referencia en una función en Java están bien definidos.
import re
import sys

def verify_parameters(variable, data_type):
    regex = data_type + '\s*(\[\s*\]\s*)+\s*[a-zA-Z_$][a-zA-Z_$0-9]*$'
    if re.match(regex, variable):
        return True
    regex = data_type + '\s+[a-zA-Z_$][a-zA-Z_$0-9]*\s*(\[\s*\]\s*)*$'
    if re.match(regex, variable):
        return True
    return False

data_type = '^(byte|short|int|long|float|double|boolean|char|String|Byte|Short|Integer|Long|Float|Double|Boolean|Character|[a-zA-Z_$][a-zA-Z_$0-9]*)'
param_valid = input('Digite los parametros que desea validar separados por comas: ').strip()
pattern = '\s*,\s*'
ids = re.split(pattern, param_valid)
no_error = True 
repeated_ids = False 
use_reserved_words = False
    
identifiers = list()
#Si usa palabra reservada
reserved_words = '^(byte|short|int|Integer|long|float|double|Double|boolean|Boolean|char|String|Byte|Short|Long|Float|Character|abstract|catch|final|implements|native|public|switch|true|false|assert|do|finally|import|new|return|synchronized|try|class|else|instanceof|null|short|this|void|break|const|enum|for|package|static|throw|volatile|continue|extends|goto|interface|private|strictfp|throws|while|case|default|if|protected|super|transient)$'
for ID in ids:
    if '[]' in ID:
        identifiers.append(ID.split('[]'))
    elif ' ' in ID:
        identifiers.append(ID.split(' '))
identifiers[:] = (identifier[1] for identifier in identifiers)
for identifier in identifiers:
    if re.match(reserved_words,identifier.strip()):
        use_reserved_words = True
    
#Verificar que identificadores no sean iguales
identifiers.clear()
for ID in ids:
    if '[]' in ID:
        identifiers.append(ID.split('[]'))
    elif ' ' in ID:
        identifiers.append(ID.split(' '))
identifiers[:] = (identifier[1] for identifier in identifiers)
for identifier in identifiers:
    if identifiers.count(identifier) > 1:
        repeated_ids = True
    
# Revisar que no haya <palabra reservada> <tipo de dato> <identificador>
for ID in ids:
    if verify_parameters(ID, data_type) == False:
        print('Error en el parametro: ', ID)
        no_error = False

if no_error == False:
    sys.exit()

if repeated_ids:
    print('Error, Hay identificadores repetidos')
    sys.exit()
    
if use_reserved_words:
    print('Error, hay identificadores usando palabras reservadas')
    sys.exit()
    
if no_error and repeated_ids == False and use_reserved_words == False:
    print('Los parametros estan bien escritos')
    sys.exit()