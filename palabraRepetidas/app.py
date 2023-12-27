import re

def contapalabra(palabra:str):
    palabras = []
    palbrasNotRep = []
    palabrasRep = []
    result = []
    pal = ''
    contador = 0
    re.sub("[^A-Za-z0-9]", "",palabra)
    print(palabra)
    palabras = palabra.lower().split()
    for i in range(len(palabras)):
        if not palabras[i] in palbrasNotRep:
            palbrasNotRep.append(palabras[i])
        else:
            palabrasRep.append(palabras[i])
    for i in palabrasRep:
        print(i)
        for j in palabrasRep:
            if i == j:
                pal = j
                contador+=1
 
    print(f"La palabra que mas se repite en la oración es: '{pal}' las veces: {contador}")
    
    
    
contapalabra("Hola, mi nombre es brais. Mi nombre completo es Brais Moure hola  hola hola(MoureDev).")