def factorial(number:int):
    if number == 1:
        return 1
    return number * factorial(number-1)






valor = factorial(7)
print(valor)