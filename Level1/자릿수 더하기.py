def solution(n):
    sum = 0 
    for i in list(map(int, list(str(n)))):
        sum += i 
    return sum 

# list sum
def solution(n):
    return sum([int(i) for i in str(n)])