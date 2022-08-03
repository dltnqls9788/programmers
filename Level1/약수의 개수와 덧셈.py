from re import L


def solution1(left, right):
    sum = 0 

    for num in range(left, right+1):
        count = 1
        for i in range(1,num//2+1):
            if num%i == 0:
                count += 1 
        
        if count % 2 == 0 :
            sum += num
        else :
            sum -= num
    return sum


def solution2(left, right):
    sum = 0 

    for i in range(left, right+1):
        if int(i**0.5) == i**0.5: # 제곱수는 약수의 개수가 홀수
            sum -= i 
        else:
            sum += i 

    return sum