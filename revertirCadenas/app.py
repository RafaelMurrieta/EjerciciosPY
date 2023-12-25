<<<<<<< HEAD
def revertir(palabra: str):
    print(palabra)
    newPalabra = []
    for i in range(len(palabra)-1, -1 , -1):
        newPalabra.append(palabra[i])
    resultado = ''.join(newPalabra)
    print(resultado)
    
=======
def revertir(palabra: str):
    print(palabra)
    newPalabra = []
    for i in range(len(palabra)-1, -1 , -1):
        newPalabra.append(palabra[i])
    resultado = ''.join(newPalabra)
    print(resultado)
    
>>>>>>> cca8414323dade681936e1d599d1daac71b40e7a
revertir("Hola mundo")