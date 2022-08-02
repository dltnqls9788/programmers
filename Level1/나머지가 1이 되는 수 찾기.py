def solution(n):
    lst = []

    for i in range(1,(n-1)+1):
        if (n-1)%i == 0:
            lst.append(i)
    
    return lst[1]