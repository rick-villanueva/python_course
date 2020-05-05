def collatz_conjecture(n):
    numbers = [n]
    
    if n <= 1:
        return [ ]
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = (n*3) + 1 
            
        numbers.append(n)
        
    return numbers

def collatz_counter(n):
    numbers = [n]
    
    if n <= 1:
        return [ ]
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = (n*3) + 1 
            
        numbers.append(n)
    
    return len(numbers)

collatz_conjecture(8)
collatz_counter(10786)