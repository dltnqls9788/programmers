n = 5
lost = 	[2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    # 여벌의 체육복이 있는 학생이 도난 당했을 경우 체육복을 빌려줄 수 없으므로 제외
    reserve_uniq = set(reserve)-set(lost) 
    lost_uniq = set(lost)-set(reserve) 


    for i in reserve_uniq:
        if i-1 in lost_uniq:
            lost_uniq.remove(i-1)
        elif i+1 in lost_uniq:
            lost_uniq.remove(i+1)

    return n-len(lost_uniq)