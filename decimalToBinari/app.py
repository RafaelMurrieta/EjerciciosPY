def transorm(number:int):
    binario = []
    while number > 0:
        compro = number % 2 
        if compro == 0:
            binario.append('0')
        else:
            binario.append('1')
        number = number//2
    
    binario.reverse()     
    binario = ''.join(binario)
    print(binario)
transorm(35)