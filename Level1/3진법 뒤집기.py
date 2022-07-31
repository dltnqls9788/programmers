def solution1(n):
    result = []
    sum = 0 

    while n!=0:
        result.append(n%3)
        n = n//3

    for i in range(len(result)):
        sum += ((3 ** (len(result)-i-1)) * result[i])

    return sum


def solution2(n):
    result = ''
    while n:
        result += str(n%3)
        n = n//3
    return int(result,3) # 3진법 -> 10진법 