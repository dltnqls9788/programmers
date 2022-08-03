def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]

    lst = [0] * 4

    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            lst[1] += 1 
        if b[i%8] == answers[i]:
            lst[2] += 1 
        if c[i%10] == answers[i]:
            lst[3] += 1

    answer = []
    for i in range(1,4):
        if lst[i] == max(lst):
            answer.append(i)
            
    return answer 