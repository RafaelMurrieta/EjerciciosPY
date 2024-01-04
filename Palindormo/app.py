import re


def palindromo(expresion:str):
    stack = []
    stack2 = {}
    expresion = expresion.lower()
    re.sub("[^A-Za-z0-9]", "",expresion)
    expresion = expresion.replace('.', '')
    expresion = expresion.replace(' ','')
    first = expresion
    for i in range(len(expresion)):
        stack.append(expresion[i])
    stack.reverse()
    expesion = ''.join(stack)
    print(expresion)
    print(first)
    if first == expesion:
        print('es igual')
    else:
        print('No es igual')
        
palindromo("Ana lleva al oso la avellana.")