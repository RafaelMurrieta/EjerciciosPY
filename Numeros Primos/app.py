<<<<<<< HEAD
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
=======
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
>>>>>>> cca8414323dade681936e1d599d1daac71b40e7a
