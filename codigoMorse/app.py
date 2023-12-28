def morse(frase: str):
    array = []
    morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',' ': '/', '?': '..——..', '.' : '.—.—.—'
}
    print(morse_code['h'])

    frase = frase.lower()
    for i in range(len(frase)):
        letra = frase[i]
        array.append(morse_code[letra]) 
    print(array)
    
morse("Hola como estas")
morse("Chocapic. Es una marca de cereales?")