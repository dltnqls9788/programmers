def solution(new_id):
    
    # 1단계
    answer = new_id.lower()

    # 2단게
    ch = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    answer = ''.join([w for w in answer if w in ch])

    # 3단계
    while '..' in answer:
        answer = answer.replace('..','.')

    # 4단계
    answer = answer.strip('.') 

    # 5단계
    if answer == '': answer += 'a'

    # 6단계
    answer = answer[:15].rstrip('.')

    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]

    return answer