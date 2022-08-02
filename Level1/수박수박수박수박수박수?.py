def solution1(n):
    answer = ''
    if n%2 == 0:
        answer += n//2 * '수박'
    else:
        answer += (n//2 * '수박' + '수')
    return answer 

def solution2(n):
    return "수박"*(n//2) + "수"*(n%2) 