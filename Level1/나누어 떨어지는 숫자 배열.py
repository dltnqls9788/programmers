def solution1(arr, divisor):
    lst = []
    for i in arr:
        if i % divisor == 0:
            lst.append(i)

    if lst == [] :
        return [-1]
    else:
        return sorted(lst)


def solution2(arr, divisor): 
    return sorted([i for i in arr if i % divisor == 0]) or [-1]