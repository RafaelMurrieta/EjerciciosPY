def amstrong(numero:int, total:int):
    # print(numero)

    if numero == 1:
        return 1
    total = numero * amstrong(numero-1, total)
    return numero * amstrong(numero-1, total)
    print(f'total',total)
    
    
    
    
    
ele=amstrong(7,0)
print(ele)