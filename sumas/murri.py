def find_sums(numbers:list, object:int)->list:
    
    def find_sum(start: int, object: int, combination:  list):
        
        #Encontrar solucion
        if object == 0:
            result.append(combination[:])
            return
        #No encontrar solucion
        if object < 0 or start == len(numbers): 
            return
        #Busqueda
        for index in range(start, len(numbers)):
            if index > start and numbers[index] == numbers[index-1]:
                continue
                
            combination.append(numbers[index])
            find_sum( index + 1, object - numbers[index], combination)
            combination.pop()
    

    numbers.sort()
    result = []
    find_sum(0, object, [])
    return result


print(find_sums([2,7,1,2,1,2],8))