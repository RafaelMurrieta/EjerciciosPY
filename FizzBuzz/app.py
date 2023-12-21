
def fasBuzz():
    for a in range(101):
        Fizz = a % 3 == 0
        Buzz = a % 5 == 0 
        
        if Fizz & Buzz:
            print("FizzBuzz");
        elif Fizz:
            print("Fizz")
        elif Buzz:
            print("Buzz")
        else:
            print(a)
        
fasBuzz()