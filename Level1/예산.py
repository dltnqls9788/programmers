def solution1(d, budget):
    d.sort()
    answer = 0 
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            answer += 1 
        else:
            break
    return answer



def solution2(d, budget):
    d.sort()  
    while budget < sum(d):
        d.pop()
    return len(d)