def solution1(s):   
    lst = ''  
    for word in s.split(' '):
        for i in range(len(word)):
            if i%2:
                lst += word[i].lower()
            else:
                lst += word[i].upper()
        lst += ' '

    return lst[:-1]


def solution2(s):
    return " ".join(map(lambda x: "".join([a.lower() if i%2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))