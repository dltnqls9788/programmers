def solution1(sizes):
    w = [] # 큰값
    h = [] # 작은값

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            w.append(sizes[i][1])
            h.append(sizes[i][0])
    
    return max(w) * max(h)


def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes) # 런타임에러