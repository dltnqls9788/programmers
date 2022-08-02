def solution1(a, b):
    sum = 0 
    if a <= b:
        for i in range(a,b+1):
            sum += i 
    else:
        for i in range(b, a+1):
            sum += i 

    return sum


def solution2(a, b):
    if a > b : 
        a, b = b, a 
    
    return sum(range(a, b+1))