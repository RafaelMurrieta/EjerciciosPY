def  fibonazzi():
    ant = 0
    ant2 = 1
    for i in range(10):
        print(ant)
        r =  ant + ant2
        ant = ant2
        ant2 = r
       

        
        
        
fibonazzi()