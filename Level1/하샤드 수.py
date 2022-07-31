def solution1(x):
    x = str(x)
    sum = 0 

    for i in range(len(x)):
        sum += int(x[i])
    
    if int(x) % sum == 0:
        return True
    else:
        return False


def solution2(x):
    return x % sum([int(c) for c in str(x)]) == 0 