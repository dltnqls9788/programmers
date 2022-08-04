def solution(arr):
    lst = []

    for i in range(len(arr)):
        if i == 0:
            lst.append(arr[i])
        elif arr[i] != arr[i-1]:
            lst.append(arr[i])
    
    return lsts