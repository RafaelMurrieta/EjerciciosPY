def areaPoligono(figura:str,base:float = None, altura:float= None):
    figura = figura.lower()
    
    if figura == 'rectangulo':
        r = base * altura
    elif figura == 'cuadrado':
        r = base * base  or altura * altura
    elif figura == 'paralelogramo':
        r = base * altura / 2
    return r

print(areaPoligono('RECTANGULO',4.2,5.5))    
print(areaPoligono('CUADRADO', 4.2))    
print(areaPoligono('PARALELOGRAMO', 10,5))