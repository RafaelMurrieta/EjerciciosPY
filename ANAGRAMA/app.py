def anagrama(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()    
    
    if len(word1) != len(word2):
        return False
    
    return set(word1) == set(word2)

resultado = anagrama("RAFA", "ROMA")
print(resultado)