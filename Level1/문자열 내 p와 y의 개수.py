def solution1(s):
    num1 = 0 
    num2 = 0 

    for i in s:
        if (i == "p") or (i == "P"):
            num1 += 1
        elif (i == "y") or (i == "Y"):
            num2 += 1

    if num1 == num2:
        return True
    else:
        return False

def solution2(s):
    return s.lower().count('p') == s.lower().count('y')