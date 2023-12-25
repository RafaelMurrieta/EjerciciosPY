def revertir(palabra: str):
    print(palabra)
    newPalabra = []
    for i in range(len(palabra)-1, -1 , -1):
        newPalabra.append(palabra[i])
    resultado = ''.join(newPalabra)
    print(resultado)
    
revertir("Hola mundo")