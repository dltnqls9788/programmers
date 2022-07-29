def solution1(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)

    check = {}
    lst = {}

    for re in report:
        a, b = re.split()

        if b not in check:
            check[b] = 1 
        else: 
            check[b] += 1

        if a not in lst : 
            lst[a] = [b]
        else: 
            if b not in lst[a]:
                lst[a] += [b]
        
    for id_, n in check.items():
        if n >= k:
            for user1, user2 in lst.items():
                if id_ in user2 :
                    answer[id_list.index(user1)] += 1 

    return answer



def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    check = {x:0 for x in id_list}

    for r in set(report):
        check[r.split()[1]] += 1 

    for r in set(report):
        if check[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer 
