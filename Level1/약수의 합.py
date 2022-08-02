def solution1(n):
    lst = []

    for i in range(1,n+1):
        if n%i == 0:
            lst.append(i)
    return sum(lst)


def solution2(n):

    return n + sum([i for i in range(1, (n//2)+1) if n % i == 0])