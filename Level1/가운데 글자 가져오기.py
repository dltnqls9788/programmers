s = "qwer"

def solution1(s):
    n = len(s) // 2

    if len(s)%2:
        return s[n]
    else:
        return s[n-1:n+1]


def solution1(s):
    return s[(len(s)-1)//2 : len(s)//2+1]