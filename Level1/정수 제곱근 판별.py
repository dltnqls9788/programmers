def solution1(num):
    x = int(num ** 0.5)
    if num == (x**2):
        return (x+1)**2
    else:
        return -1


def solution2(num):
    x = num ** 0.5

    if x % 1 == 0:
        return (x+1)**2
    else:
        return -1 