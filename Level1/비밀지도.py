def check(arr, n):
    total = []
    for i in arr:
        lst = []
        for j in range(n):
            if i % 2 == 1:
                lst.append('#')
            else:
                lst.append(' ')
            
            i //= 2 

        total.append(''.join(list(reversed(lst))))
    
    return total 


def solution(n, arr1, arr2):
    lst1 = check(arr1, n)
    lst2 = check(arr2, n)

    answer = []
    for i in range(n):
        lst = []
        for j in range(n):
            if (lst1[i][j] == ' ') & (lst2[i][j] == ' '):
                lst.append(' ')
            else:
                lst.append('#')
        
        answer.append(''.join(lst))
    
    return answer