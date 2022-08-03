def solution1(absolutes, signs):
    sum = 0 
    
    for i in range(len(absolutes)):
        if signs[i]:
            sum += absolutes[i]
        else:
            sum += -absolutes[i]
    return sum 


def solution2(absolutes, signs):
    sum = 0 
    for absolute, sign in zip(absolutes, signs):
        if sign:
            sum += absolute
        else:
            sum += -absolute 
    return sum 