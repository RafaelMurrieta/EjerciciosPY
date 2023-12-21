def numerosPrimos():
    numeros_primos = []
    for i in range(2, 100):
        primo = True
        for a in range(2, i):
            if i % a == 0:
                primo = False
                break
        if primo:
            numeros_primos.append(i)
    print(numeros_primos)

numerosPrimos()
