# Determinar que los parámetros que pasan por valor o referencia en una función en Java están bien definidos.
import re
import sys

def verificarParam(elem, reserv):
    r2 = reserv + '\s*(\[\s*\]\s*)+\s*[a-zA-Z_$][a-zA-Z_$0-9]*$'
    if re.match(r2, elem):
        return True
    r3 = reserv + '\s+[a-zA-Z_$][a-zA-Z_$0-9]*\s*(\[\s*\]\s*)*$'
    if re.match(r3, elem):
        return True
    return False

reserv = '^(byte|short|int|long|float|double|boolean|char|String|Byte|Short|Integer|Long|Float|Double|Boolean|Character|[a-zA-Z_$][a-zA-Z_$0-9]*)'
sw = 1
while sw == 1:
    param_valid = input('Digite los parametros que desea validar separados por comas: ').strip()
    pattern = '\s*,\s*'
    elems = re.split(pattern, param_valid)
    noHayError = True 
    hayIdsRepetidos = False 
    idUsaPalabraReserv = False
    elemsAVerificar = 0
    ide = elems.copy() #Vector de identificadores
    
    for  i in range(len(elems)):
        elems[i] = elems[i].strip()
        if len(elems[i]) > 4:
            if elems[i][0:5] == 'final':
                elems[i] = elems[i][5].strip()
        
        if elems[i].index('[') == -1 and elems[i].index(']') == -1:
            if elems.index(' ') > 1:
                valor = re.split('\s+',elems[i].strip())
                if len(valor) == 2:
                    elemsAVerificar += 1
                    ide[elemsAVerificar] = valor[1]
        else:
            corchUltimoIdx = elems[i].rindex(']')
            if corchUltimoIdx > -1:
                if corchUltimoIdx == len(elems[i]) - 1:
                    primerCorch = elems[i].index('[')
                    if primerCorch > -1:
                        end = primerCorch
                        valor = re.split('\s+',elems[i][0:end].Trim())
                        if len(valor) == 2:
                            elemsAVerificar += 1
                            ide[elemsAVerificar] = valor[1]
            elif corchUltimoIdx < len(elems[i]) - 1:
                elemsAVerificar += 1
                start = corchUltimoIdx + 1
                ide[elemsAVerificar] = elems[i].Substring(start).Trim()
    
    v = '^(byte|short|int|Integer|long|float|double|Double|boolean|Boolean|char|String|Byte|Short|Long|Float|Character|abstract|catch|final|implements|native|public|switch|true|false|assert|do|finally|import|new|return|synchronized|try|class|else|instanceof|null|short|this|void|break|const|enum|for|package|static|throw|volatile|continue|extends|goto|interface|private|strictfp|throws|while|case|default|if|protected|super|transient)$'
    for y in range(elemsAVerificar):
        if re.match(v,ide[y].strip()):
             idUsaPalabraReserv = True #Si usa palabra reservada
    
    #Verificar que identificadores no sean iguales
    for y in range(elemsAVerificar - 1):
        for j in range(y+1, len(elems)):
            if ide[y] == ide[j]:
                hayIdsRepetidos = True
    
    #// Ej.: final int a
    for i in range(len(elems)):
        if verificarParam(elems[i], reserv) == False:
            print('Error en el parametro: ', (i+1))
            noHayError = False
    
    if hayIdsRepetidos:
        print('Error, Hay identificadores repetidos')
    
    if idUsaPalabraReserv:
        print('Error, hay identificadores usando palabras reservadas')
    
    if noHayError and hayIdsRepetidos == False and idUsaPalabraReserv == False:
        print('Los parametros estan bien escritos')
        
    sw = int(input('Desea continuar? (1: sí / cualquier otro número: no): '))
    if sw != 1:
        sys.exit()