# Determinar que los parámetros que pasan por value o referencia en una función en Java están bien definidos.
import re
import sys

def verify_parameters(elem, reserved_words):
    regex = reserved_words + '\s*(\[\s*\]\s*)+\s*[a-zA-Z_$][a-zA-Z_$0-9]*$'
    if re.match(regex, elem):
        return True
    regex = reserved_words + '\s+[a-zA-Z_$][a-zA-Z_$0-9]*\s*(\[\s*\]\s*)*$'
    if re.match(regex, elem):
        return True
    return False

reserved_words = '^(byte|short|int|long|float|double|boolean|char|String|Byte|Short|Integer|Long|Float|Double|Boolean|Character|[a-zA-Z_$][a-zA-Z_$0-9]*)'
verify_more = 1
while verify_more == 1:
    param_valid = input('Digite los parametros que desea validar separados por comas: ').strip()
    pattern = '\s*,\s*'
    elems = re.split(pattern, param_valid)
    no_error = True 
    repeated_ids = False 
    use_reserved_words = False
    verify_this_elements = 0
    ids = elems.copy() #Vector de identificadores
    
    for  i in range(len(elems)):
        elems[i] = elems[i].strip()
        if len(elems[i]) > 4:
            if elems[i][0:5] == 'final':
                elems[i] = elems[i][5].strip()
        
        if '[' not in elems[i] and ']' not in elems[i]:
            if ' ' in elems:
                value = re.split('\s+',elems[i].strip())
                if len(value) == 2:
                    verify_this_elements += 1
                    ids[verify_this_elements] = value[1]
        else:
            last_corch_idx = elems[i].rindex(']')
            if last_corch_idx > -1:
                if last_corch_idx == len(elems[i]) - 1:
                    first_corch = elems[i].index('[')
                    if first_corch > -1:
                        end = first_corch
                        value = re.split('\s+',elems[i][0:end].strip())
                        if len(value) == 2:
                            verify_this_elements += 1
                            ids[verify_this_elements] = value[1]
            elif last_corch_idx < len(elems[i]) - 1:
                verify_this_elements += 1
                start = last_corch_idx + 1
                ids[verify_this_elements] = elems[i][start:].strip()
    
    #Si usa palabra reservada
    v = '^(byte|short|int|Integer|long|float|double|Double|boolean|Boolean|char|String|Byte|Short|Long|Float|Character|abstract|catch|final|implements|native|public|switch|true|false|assert|do|finally|import|new|return|synchronized|try|class|else|instanceof|null|short|this|void|break|const|enum|for|package|static|throw|volatile|continue|extends|goto|interface|private|strictfp|throws|while|case|default|if|protected|super|transient)$'
    for y in range(verify_this_elements):
        if re.match(v,ids[y].strip()):
             use_reserved_words = True
    
    #Verificar que identificadores no sean iguales
    for y in range(verify_this_elements - 1):
        for j in range(y+1, len(elems)):
            if ids[y] == ids[j]:
                repeated_ids = True
    
    #// Ej.: final int a
    for i in range(len(elems)):
        if verify_parameters(elems[i], reserved_words) == False:
            print('Error en el parametro: ', (i+1))
            no_error = False
    
    if repeated_ids:
        print('Error, Hay identificadores repetidos')
    
    if use_reserved_words:
        print('Error, hay identificadores usando palabras reservadas')
    
    if no_error and repeated_ids == False and use_reserved_words == False:
        print('Los parametros estan bien escritos')
        
    verify_more = int(input('Desea continuar? (1: sí / cualquier otro número: no): '))
    if verify_more != 1:
        sys.exit()